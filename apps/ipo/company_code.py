import aiohttp
import asyncio
from datetime import datetime, timedelta

import re
from datetime import datetime

import bs4
from bs4 import BeautifulSoup
from db.database import async_session
from db.dals.company_dal import Company
from utilities.time_measure import timeit
from apps.ipo.agents import get_user_agents
from config.config_log import logging
from async_retrying import retry

logger = logging.getLogger("info-logger")


async def is_initialze(session) -> bool:
    instance = Company(session)
    if await instance.get_one() is None:
        # DB가 텅텅 비었음
        return True
    # 이미 데이터가 있음.
    return False


async def get_code(a_tag):
    try:
        href = a_tag["href"]
        company_code = re.search("code=(.+)&", href).group(1)
        return company_code
    except KeyError as err:
        logger.error(err)
    except AttributeError as err:
        logger.error(err)


async def is_listing_date(this_year, listing_date):
    return (
        datetime.strptime(f"{this_year}.{listing_date.string.strip()}", "%Y.%m.%d")
        + timedelta(days=1)
        > datetime.now()
    )


async def belong_to_update(demand_forecast_date, listing_date, this_year, ci_code, ipo_companies):
    if demand_forecast_date != "공모철회" and listing_date.string is None:
        ipo_companies.append(ci_code)
    elif demand_forecast_date != "공모철회" and await is_listing_date(this_year, listing_date):
        ipo_companies.append(ci_code)
    elif demand_forecast_date == "공모철회" and listing_date.string is None:
        ipo_companies.append(ci_code)
    elif demand_forecast_date == "공모철회" and await is_listing_date(this_year, listing_date):
        ipo_companies.append(ci_code)
    return


async def get_name_n_code(td_name):
    try:
        a_tag = td_name.select_one('a[href*="view_pg"][class=""]')
        href = a_tag["href"]
        company_code = re.search("code=(.+)&", href).group(1)
        company_name = a_tag.select_one("font").text.strip().replace(".", "")
        return company_code, company_name
    except KeyError as err:
        logger.error(err)
    except AttributeError as err:
        logger.error(err)


async def get_years(year):
    current_year = datetime.now().year
    for k in range(year, current_year + 1):
        yield k


@retry(attempts=100)
async def scrape_company_codes(year=2021):
    ipo_companies = []
    delisted_companies = []
    header = await get_user_agents()
    this_year = str(datetime.now().year)
    async for year in get_years(year):
        logger.debug("연도", year)
        page_data = None
        page = 1

        while page_data is None:
            url = f"http://www.ipostock.co.kr/sub03/ipo02.asp?str4={year}&str5=all&page={page}"
            logger.debug(f"page: {page}, url: {url}")
            page += 1

            # DB에 데이터가 1개라도 있으면 당해년도로
            # DB에 데이터가 없으면 2021년도부터 모두 가져옴
            async with async_session() as session:
                async with session.begin():
                    is_initialized = await is_initialze(session)

            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=header) as resp:
                        soup = BeautifulSoup(await resp.text(), "lxml")

            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                logger.error("Request failed, retrying in 5 seconds...")
                logger.error(e)
                await asyncio.sleep(1)

            page_data = soup.select_one('td[colspan="9"]')
            if page_data is not None:
                logger.debug("페이지에 기업이 없습니다. 다음 연도로 전환됩니다")
                break
            table = soup.select_one(
                "#print > table >  tr:nth-child(4) > td > table >  tr:nth-child(3) > td > table >  tr:nth-child(4) > td > table"
            )

            for idx, tr in enumerate(table, 0):
                if isinstance(tr, bs4.element.Tag) and tr is not None:
                    if not is_initialized:
                        ci_name = tr.select_one("td:nth-child(3)")
                        listing_date = tr.select_one("td:nth-child(7)")

                        if str(year) == this_year and ci_name is not None:
                            demand_forecast_date = (
                                tr.select_one("td:nth-child(2)").get_text().strip()
                            )
                            ci_name = (
                                tr.select_one("td:nth-child(3)").get_text().replace(" ", "").strip()
                            )
                            ci_code = tr.select_one("td:nth-child(3) a")
                            ci_code = await get_code(ci_code)
                            listing_date = tr.select_one("td:nth-child(7)")
                            await belong_to_update(
                                demand_forecast_date,
                                listing_date,
                                this_year,
                                ci_code,
                                ipo_companies,
                            )

                    else:
                        td = tr.find("td", {"width": "120"})
                        if td is not None:
                            td_name = tr.find("td", {"width": "*"})
                            delisting = td.text.strip()
                            company_code, company_name = await get_name_n_code(td_name)

                            if delisting == "공모철회":
                                logger.info(f"공모철회 회사명 : {company_name}/ 코드:{company_code}")
                                delisted_companies.append(company_code)
                            else:
                                ipo_companies.append(company_code)
    return ipo_companies + delisted_companies


if __name__ == "__main__":

    @timeit
    async def main():
        result = await scrape_company_codes()
        print(len(result))

    asyncio.run(main())
