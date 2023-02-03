from typing import Type, Union
import datetime
from sqlalchemy import Column, DateTime, Float, String, Text, text, ForeignKey, SMALLINT
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
metadata = Base.metadata


class CompanyInfoGeneral(Base):
    __tablename__ = "company_info_general"
    __table_args__ = {"comment": "기업정보 기본"}

    ci_idx: int = Column(INTEGER(11), primary_key=True, autoincrement=True)
    ci_market_separation: str = Column(String(255), comment="시장구분")
    ci_progress: str = Column(String(255), comment="진행단계")
    ci_name: str = Column(String(255), nullable=False, comment="기업명")
    ci_code: str = Column(String(255), nullable=False, comment="기업코드")
    ci_list_type: str = Column(String(255), comment="상장유형")
    ci_review_c_date: str = Column(String(50), comment="심사청구일(Y/m/d)")
    ci_review_a_date: str = Column(String(50), comment="심사승인일(Y/m/d)")
    ci_face_value: int = Column(INTEGER(11), comment="액면가")
    ci_ceo: str = Column(String(50), comment="대표이사")
    ci_tel: str = Column(String(50), comment="대표전화")
    ci_homepage: str = Column(String(255), comment="홈페이지")
    ci_establishment_date: str = Column(String(50), comment="설립일(Y/m/d)")
    ci_company_separation: str = Column(String(255), comment="기업구분")
    ci_brn: str = Column(String(255), comment="사업자등록번호")
    ci_settlement_month: int = Column(INTEGER(11), comment="결산월")
    ci_worker_cnt: int = Column(INTEGER(11), comment="종업원수")
    ci_industries: str = Column(String(255), comment="업종")
    ci_important_product: str = Column(String(255), comment="주요제품")
    ci_stocks_separation: str = Column(String(255), comment="주권구분")
    ci_lead_manager: str = Column(String(255), comment="주간사")
    ci_address: str = Column(String(255), comment="본점소재지")
    ci_turnover: float = Column(Float(asdecimal=True), comment="청구시 매출액 (단위 : 억원)")
    ci_before_corporate_tax: float = Column(Float(asdecimal=True), comment="법인세 차감전 순이익 (단위 : 억원)")
    ci_net_profit: float = Column(Float(asdecimal=True), comment="청구시 순이익 (단위 : 억원)")
    ci_capital: float = Column(Float(asdecimal=True), comment="청구시 자기자본 (단위 : 억원)")
    ci_largest_shareholder: str = Column(String(255), comment="청구시 최대주주")
    ci_largest_shareholder_rate: float = Column(Float(asdecimal=True), comment="최대 주주 비율")
    ci_po_expected_price: str = Column(String(50), comment="[[ 삭제요청 ]] 공모(예정) 발행가 (범위 : '~'로 자르기)")
    ci_po_expected_stocks: int = Column(INTEGER(11), nullable=False, comment="공모(예정) 주식수")
    ci_po_expected_amount: str = Column(String(50), comment="[[ 삭제요청 ]] 공모(예정) 금액 (범위 : '~'로 자르기)")
    ci_listing_expected_stocks: int = Column(INTEGER(11), comment="상장(예정) 주식수")
    ci_before_po_capital: float = Column(Float(asdecimal=True), comment="공모전 자본금 (단위 : 억원)")
    ci_before_po_stocks: int = Column(BIGINT(20), comment="공모전 발행주식주")
    ci_after_po_capital: float = Column(Float(asdecimal=True), comment="공모후 자본금 (단위 : 억원)")
    ci_after_po_stocks: int = Column(BIGINT(20), comment="공모후 발행주식주")
    ci_most_subscription: str = Column(String(50), comment="[[ 삭제요청 ]] 최대주주 (앱용)")
    ci_big_ir_plan: str = Column(String(50), comment="[[ 삭제요청 ]] 대규모 IR 일정")
    ci_demand_forecast_date: str = Column(String(50), comment="수요예측일 (범위 : '~'로 자르기)")
    ci_public_subscription_date: str = Column(String(50), comment="공모청약일 (범위 : '~'로 자르기)")
    ci_refund_date: str = Column(String(50), comment="환불일")
    ci_payment_date: str = Column(String(50), comment="납입일")
    ci_listing_date: str = Column(String(50), comment="상장일")
    ci_hope_po_price: str = Column(String(50), comment="희망 공모 가격 (범위 : '~'로 자르기)")
    ci_hope_po_amount: str = Column(String(50), comment="희망 공모 금액 (단위 : 억원, 범위 : '~'로 자르기)")
    ci_confirm_po_price: int = Column(INTEGER(11), comment="확정 공모 가격")
    ci_confirm_po_amount: float = Column(Float(asdecimal=True), comment="확정 공모 금액  (단위 : 억원)")
    ci_subscription_warrant_money_rate: str = Column(String(50), comment="청약증거금율")
    ci_subscription_competition_rate: str = Column(String(50), comment="청약경쟁률")
    ci_public_offering_stocks: str = Column(String(255), comment="공모주식수 ( 주,모집률 : '/'로 자르기)")
    ci_professional_investor_stock: int = Column(INTEGER(11), comment="전문투자자 주")
    ci_professional_investor_rate: int = Column(INTEGER(11), comment="전문투자자 모집율")
    ci_esa_stock: int = Column(INTEGER(11), comment="우리사주조합 주")
    ci_esa_rate: int = Column(INTEGER(11), comment="우리사주조합 모집율")
    ci_general_subscriber_stock: int = Column(INTEGER(11), comment="일반청약자 주")
    ci_general_subscriber_rate: int = Column(INTEGER(11), comment="일반청약자 모집율")
    ci_overseas_investor_stock: int = Column(INTEGER(11), comment="해외투자자 주")
    ci_overseas_investor_rate: int = Column(INTEGER(11), comment="해외투자자 모집율")
    ci_noted_items_check: str = Column(String(50), comment="참고사항 활성화 (N:비활성화 , Y:활성화)")
    ci_guidelines_check: str = Column(String(50), comment="안내사항 활성화 (N:비활성화 , Y:활성화)")
    ci_small_ir_plan: str = Column(String(255), comment="[[ 삭제요청 ]] 소규모 IR 일정")
    ci_receipt_way: str = Column(String(255), comment="[[ 삭제요청 ]] 접수방법")
    ci_receipt_place: str = Column(String(255), comment="[[ 삭제요청 ]] 접수장소")
    ci_ask_tel: str = Column(String(255), comment="[[ 삭제요청 ]] 문의전화")
    ci_organizer_homepage: str = Column(String(255), comment="[[ 삭제요청 ]] 주관사 홈페이지")
    ci_most_quantity: int = Column(BIGINT(20), comment="[[ 삭제요청 ]] 최고신청수량")
    ci_unit: str = Column(String(255), comment="[[ 삭제요청 ]] 단위 ( 주,원 : '/'로 자르기)")
    ci_competition_rate: str = Column(String(255), comment="단순 기관 경쟁률")
    ci_current_ratio: int = Column(INTEGER(11), comment="유동비율")
    ci_like: int = Column(INTEGER(11), server_default=text("0"), comment="좋아요")
    ci_dislike: int = Column(INTEGER(11), server_default=text("0"), comment="싫어요")
    ci_vitalization1: str = Column(String(50), comment="탭 활성화 [기업정보] (Y/N)")
    ci_vitalization2: str = Column(String(50), comment="탭 활성화 [회사개요] (Y/N)")
    ci_vitalization3: str = Column(String(50), comment="탭 활성화 [주주구성] (Y/N)")
    ci_vitalization4: str = Column(String(50), comment="탭 활성화 [재무정보] (Y/N)")
    ci_vitalization5: str = Column(String(50), comment="탭 활성화 [공모정보] (Y/N)")
    ci_vitalization6: str = Column(String(50), comment="탭 활성화 [수요예측] (Y/N)")
    ci_demand_schedule: str = Column(String(50), comment="IPO공모관리 수요예측일정 추가 (Y/N)")
    ci_demand_schedule_state: str = Column(
        String(50), comment="IPO공모관리 수요예측일정 상태 (upload/delete/modify/real_delete)"
    )
    ci_demand_schedule_datetime: datetime = Column(DateTime, comment="IPO공모관리 수요예측일정 업데이트 날짜")
    ci_demand_result: str = Column(String(50), comment="IPO공모관리 수요예측결과 추가 (Y/N)")
    ci_demand_result_state: str = Column(
        String(50), comment="IPO공모관리 수요예측결과 상태 (upload/delete/modify/real_delete)"
    )
    ci_demand_result_datetime: datetime = Column(DateTime, comment="IPO공모관리 수요예측결과 업데이트 날짜")
    ci_public_schedule: str = Column(String(50), comment="IPO공모관리 공모청약일정 추가 (Y/N)")
    ci_public_schedule_state: str = Column(
        String(50), comment="IPO공모관리 공모청약일정 상태 (upload/delete/modify/real_delete)"
    )
    ci_public_schedule_datetime: datetime = Column(DateTime, comment="IPO공모관리 공모청약일정 업데이트 날짜")
    ci_datetime: datetime = Column(DateTime, nullable=False)

    shareholders = relationship("CompanyInfoShareholder", back_populates="company")
    predictions = relationship("CompanyInfoPrediction", back_populates="company")
    subscribers = relationship("CompanyInfoSubscriber", back_populates="company")
    financials = relationship("CompanyInfoFinancial", back_populates="company")
    app_calendars = relationship("AppCalendar", back_populates="company")


class CompanyInfoShareholder(Base):
    __tablename__ = "company_info_shareholder"
    __table_args__ = {"comment": "주주구성 보호예수/유통가능"}

    cis_idx: int = Column(INTEGER(11), primary_key=True, autoincrement=True)
    ci_idx: int = Column(
        INTEGER(11),
        ForeignKey("company_info_general.ci_idx", ondelete="CASCADE"),
        comment="기업 idx",
        nullable=True,
    )
    ci_category: int = Column(SMALLINT(), comment="구분 (1:보호예수매도금지 , 2:유통가능)")
    ci_category_name: str = Column(String(50), comment="구분 이름")
    ci_normal_stocks: int = Column(BIGINT(20), comment="보유주식 보통주")
    ci_first_stocks: int = Column(INTEGER(11), comment="보유주식 우선주")
    ci_share_rate: float = Column(Float(asdecimal=True), comment="공모후 보통주 지분율")
    ci_protection_date: str = Column(String(50), comment="보호예수기간")
    ci_datetime: datetime = Column(DateTime, server_default=text("'0000-00-00 00:00:00'"))

    company = relationship("CompanyInfoGeneral", back_populates="shareholders")


class CompanyInfoPrediction(Base):
    __tablename__ = "company_info_prediction"
    __table_args__ = {"comment": "수요예측결과"}

    cip_idx = Column(INTEGER(11), primary_key=True)
    ci_idx = Column(
        INTEGER(11),
        ForeignKey("company_info_general.ci_idx", ondelete="CASCADE"),
        comment="기업 idx",
        nullable=True,
    )
    ci_price: str = Column(String(255), comment="가격")
    ci_incidence: int = Column(INTEGER(11), comment="건수")
    ci_incidence_specific_gravity: float = Column(Float(asdecimal=True), comment="건수비중")
    ci_participation: int = Column(BIGINT, comment="참여수량")
    ci_participation_specific_gravity: float = Column(Float(asdecimal=True), comment="참여수량비중")
    ci_datetime: datetime = Column(DateTime, server_default=text("'0000-00-00 00:00:00'"))

    company = relationship("CompanyInfoGeneral", back_populates="predictions")


class CompanyInfoSubscriber(Base):
    __tablename__ = "company_info_subscriber"
    __table_args__ = {"comment": "공모정보 일반청약자 상세"}

    cis_idx: int = Column(INTEGER(11), primary_key=True)
    ci_idx: int = Column(
        INTEGER(11),
        ForeignKey("company_info_general.ci_idx", ondelete="CASCADE"),
        comment="기업 idx",
        nullable=True,
    )
    ci_stock_firm: str = Column(String(50), server_default=text("'0'"), comment="증권사")
    ci_assign_quantity: int = Column(INTEGER(11), server_default=text("0"), comment="배정수량")
    ci_limit: int = Column(INTEGER(11), server_default=text("0"), comment="청약한도")
    ci_note: str = Column(String(50), comment="비고")
    ci_datetime: datetime = Column(DateTime, server_default=text("'0000-00-00 00:00:00'"))

    company = relationship("CompanyInfoGeneral", back_populates="subscribers")


class CompanyInfoFinancial(Base):
    __tablename__ = "company_info_financial"
    __table_args__ = {"comment": "재무정보 (단위 : 억원 , 소수점 첫째자리(천만) 까지 표기)"}

    cif_idx: int = Column(INTEGER(11), primary_key=True)
    ci_idx: int = Column(
        INTEGER(11),
        ForeignKey("company_info_general.ci_idx", ondelete="CASCADE"),
        comment="기업 idx",
        nullable=True,
    )
    cif_order: int = Column(INTEGER(11), server_default=text("0"), comment="순서")
    ci_category1: str = Column(String(50), comment="구분1")
    ci_category2: str = Column(String(50), comment="구분2")
    ci_current_asset: float = Column(Float(asdecimal=True), comment="유동자산")
    ci_non_current_asset: float = Column(Float(asdecimal=True), comment="비유동자산")
    ci_current_liability: float = Column(Float(asdecimal=True), comment="유동부채")
    ci_non_current_liability: float = Column(Float(asdecimal=True), comment="비유동부채")
    ci_capital: float = Column(Float(asdecimal=True), comment="자본금")
    ci_capital_surplus: float = Column(Float(asdecimal=True), comment="자본잉여금")
    ci_earned_surplus: float = Column(Float(asdecimal=True), comment="이익잉여금")
    ci_other_capital_items: float = Column(Float(asdecimal=True), comment="기타 자본 항목")
    ci_turnover: float = Column(Float(asdecimal=True), comment="매출액")
    ci_business_profits: float = Column(Float(asdecimal=True), comment="영업이익")
    ci_net_income: float = Column(Float(asdecimal=True), comment="당기순이익")
    ci_datetime: datetime = Column(DateTime, server_default=text("'0000-00-00 00:00:00'"))

    company = relationship("CompanyInfoGeneral", back_populates="financials")


class AppCalendar(Base):
    __tablename__ = "app_calendar"
    __table_args__ = {"comment": "앱 캘린더 관리"}

    ac_idx: int = Column(INTEGER(11), primary_key=True)
    ci_idx: int = Column(
        INTEGER(11),
        ForeignKey("company_info_general.ci_idx", ondelete="CASCADE"),
        comment="기업 idx",
        nullable=True,
    )
    ac_sdate: str = Column(String(50), comment="일정 시작일자 (yyyy-mm-dd)")
    ac_edate: str = Column(String(50), comment="일정 종료일자 (yyyy-mm-dd)")
    ac_category: int = Column(INTEGER(11), comment="1:청약일, 2:상장일, 3:환불일, 4:수요예측")
    ac_category_name: str = Column(String(50), comment="구분명")
    ac_company_name: str = Column(String(50), comment="회사명")
    ac_vitalize: str = Column(String(50), comment="Y:활성화, N:비활성화")
    ac_datetime: datetime = Column(DateTime)

    company = relationship("CompanyInfoGeneral", back_populates="app_calendars")


if __name__ == "__main__":
    import asyncio
    from db.database import async_session, engine
    from sqlalchemy import select, func
    from sqlalchemy import and_
    from sqlalchemy.orm import Session, selectinload
    from sqlalchemy import select, func
    from db.models import (
        CompanyInfoShareholder as Shareholder,
        CompanyInfoFinancial as Financial,
        CompanyInfoSubscriber as Subscriber,
        CompanyInfoPrediction as Prediction,
        CompanyInfoGeneral as General,
        AppCalendar as Calendar,
    )
    from db.dals.company_dal import Company
    from db import database

    async def main():
        # print(database.DB_URL, database.ASYNC_DB_URL)
        async with async_session() as session:
            async with session.begin():
                ci_code = 344860
                stmt = (
                    select(CompanyInfoGeneral)
                    .where(CompanyInfoGeneral.ci_code == ci_code)
                    .execution_options(populate_existing=True)
                    .options(
                        selectinload(CompanyInfoGeneral.shareholders),
                        selectinload(CompanyInfoGeneral.subscribers),
                        selectinload(CompanyInfoGeneral.financials),
                        selectinload(CompanyInfoGeneral.app_calendars),
                        selectinload(CompanyInfoGeneral.predictions),
                    )
                )

                # will refresh all matching User objects as well as the related
                # Address objects
                cig = await session.execute(stmt)
                result = cig.scalars().first()
                # for field_name in Shareholder.__dict__:
                #     f"{i}"
                # for i in result.shareholders:
                #     print(
                #         i.ci_idx,
                #         i.cis_idx,
                #     )
                print(result.ci_idx, result.ci_code, result.ci_name, result.ci_market_separation)

                print(result.shareholders)
                print(result.subscribers)
                print(result.financials)
                print(result.predictions)
                # print(dict(result.shareholders))
            await engine.dispose()

    asyncio.run(main(), debug=True)
