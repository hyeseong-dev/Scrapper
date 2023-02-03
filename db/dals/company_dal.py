import asyncio
from typing import List, Optional
from sqlalchemy import select, func
from config.settings import settings

from utilities.time_measure import timeit
from sqlalchemy import and_
from sqlalchemy.orm import Session, selectinload
from db.models import (
    CompanyInfoShareholder as Shareholder,
    CompanyInfoFinancial as Financial,
    CompanyInfoSubscriber as Subscriber,
    CompanyInfoPrediction as Prediction,
    CompanyInfoGeneral as General,
    AppCalendar as Calendar,
)
from schemas.calendar import CalendarCreateSchema
from schemas.general import GeneralCreateSchema
from schemas.financial import FinancialCreateSchema
from schemas.prediction import PredictionCreateSchema
from schemas.shareholder import ShareholderCreateSchema
from schemas.subscriber import SubscriberCreateSchema

from db.database import async_session, engine
from config.config_log import logging

logger = logging.getLogger("info-logger")

DELISTING = settings.DELISTING


class Company:
    def __init__(self, db_session: Session):
        self._db_session = db_session

    async def create(
        self,
        general: General,
        shareholders: List[Shareholder],
        financials: List[Financial],
        subscribers: List[Subscriber],
        predictions: List[Prediction],
        calendars: List[Calendar],
    ) -> bool:

        new_company = general
        new_company.shareholders = shareholders
        new_company.financials = financials
        new_company.subscribers = subscribers
        new_company.predictions = predictions
        new_company.app_calendars = calendars

        self._db_session.add(new_company)
        await self._db_session.flush()
        return True

    async def get_one(self) -> General:
        q = await self._db_session.execute(select(General).limit(1))
        return q.first()

    async def get_count(self) -> General:
        count = await self._db_session.scalar(select(func.count(General.ci_idx)))
        return count
        # return True if q.first() else False

    async def get_all_companies(self) -> List[General]:
        q = await self._db_session.execute(
            select(General).order_by(General.ci_demand_forecast_date)
        )
        return q.scalars().all()

    async def get_all_delisted_companies_name(self) -> List[str]:
        q = await self._db_session.execute(
            select([General.ci_name])
            .where(General.ci_demand_forecast_date != DELISTING)
            .order_by(General.ci_datetime)
        )
        return [row[0][:10] for row in q]

    async def read(self, ci_code: str) -> Optional[General]:
        q = await self._db_session.execute(
            select(General)
            .where(General.ci_code == ci_code)
            .execution_options(populate_existing=True)
            .options(
                selectinload(General.shareholders),
                selectinload(General.subscribers),
                selectinload(General.financials),
                selectinload(General.app_calendars),
                selectinload(General.predictions),
            )
        )
        result = q.scalars().first()
        if result:
            return result
        return

    async def update(
        self,
        general: General,
        shareholders: List[Shareholder],
        financials: List[Financial],
        subscribers: List[Subscriber],
        predictions: List[Prediction],
        calendars: List[Calendar],
    ) -> bool:

        existing_general = await self.read(general.ci_code)

        existing_general.shareholders = []
        existing_general.financials = []
        existing_general.subscribers = []
        existing_general.predictions = []
        existing_general.app_calendars = []

        existing_general.shareholders = shareholders
        existing_general.financials = financials
        existing_general.subscribers = subscribers
        existing_general.predictions = predictions
        existing_general.app_calendars = calendars

        return True

    async def upsert(
        self,
        general: GeneralCreateSchema,
        shareholders: List[ShareholderCreateSchema],
        financials: List[FinancialCreateSchema],
        subscribers: List[SubscriberCreateSchema],
        predictions: List[PredictionCreateSchema],
        calendars: List[CalendarCreateSchema],
    ):

        ci_code = general.ci_code
        general = General(**general.dict())
        shareholders = [Shareholder(**shareholder.dict()) for shareholder in shareholders]
        financials = [Financial(**financial.dict()) for financial in financials]
        subscribers = [Subscriber(**subscriber.dict()) for subscriber in subscribers]
        predictions = [Prediction(**prediction.dict()) for prediction in predictions]
        calendars = [Calendar(**calendar.dict()) for calendar in calendars]

        existed_general = await self.read(ci_code)
        if existed_general is not None:
            logger.info(f"existed_ci_code: {existed_general.ci_code}")
            result = await self.update(
                general,
                shareholders,
                financials,
                subscribers,
                predictions,
                calendars,
            )
            if result:
                logger.info("기업 데이터를 수정하였습니다")
                return True
            logger.info("기업 데이터에 실패하였습니다.")
            return False

        else:
            result = await self.create(
                general,
                shareholders,
                financials,
                subscribers,
                predictions,
                calendars,
            )
            if result:
                logger.info("기업 데이터를 등록 하였습니다")
                return True
            logger.info("기업 데이터 수정에 실패하였습니다.")
            return False


if __name__ == "__main__":
    from temp import raw_data

    @timeit
    async def main():
        async with async_session() as session:
            # async with session.begin():
            company_dal: General = Company(session)
            # await company_dal.create(
            #     raw_data.general_dict,
            #     raw_data.shareholders_dict,
            #     raw_data.financials_dict,
            #     raw_data.subscribers_dict,
            #     raw_data.predictions_dict,
            # )
            #     r: General = await company_dal.read("툴젠")
            #     print(r.ci_name, r.ci_demand_forecast_date)
            # async with session.begin():
            #     r = await company_dal.delist(r.ci_name)
            #     print(r)
            async with session.begin():
                # rs: General = await company_dal.get_one()
                # print([r.ci_name for r in rs])
                # print(rs)
                rs = await company_dal.read(358570)
                print(rs)
                print(rs.shareholders)
                print(rs.subscribers)
                print(rs.predictions)
                print(rs.financials)
                # await company_dal.update(rs)
            # r = await company_dal.get_all_delisted_companies_name()
            # print(r, len(r))
        await engine.dispose()

    asyncio.run(main(), debug=True)
