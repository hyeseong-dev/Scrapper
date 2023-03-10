import re
import string
from typing import List
from datetime import datetime

from enum import Enum
from pydantic import BaseModel, validator, Field

from utilities import converters

# from schemas.financial import CompanyInfoFinancialSchema
# from schemas.prediction import CompanyInfoPredictionSchema
# from schemas.shareholder import CompanyInfoShareholderSchema
# from schemas.prediction import CompanyInfoPredictionSchema
# from schemas.subscriber import CompanyInfoSubscriberSchema
# from schemas.calendar import AppCalendarSchema
#


class State(Enum):
    MODIFY = "modify"
    DELETE = "delete"
    REAL_DELETE = "real_delete"
    UPLOAD = "upload"


class GeneralBase(BaseModel):
    ci_market_separation: str = ""
    ci_progress: str = ""
    ci_name: str = ""
    ci_code: str = ci_name
    ci_list_type: str = ""
    ci_review_c_date: str = ""
    ci_review_a_date: str = ""
    ci_face_value: int = 0
    ci_ceo: str = ""
    ci_tel: str = ""
    ci_homepage: str = ""
    ci_establishment_date: str = ""
    ci_company_separation: str = ""
    ci_brn: str = ""
    ci_settlement_month: int = 0  # 결산월
    ci_worker_cnt: int = 0
    ci_industries: str = ""
    ci_important_product: str = ""
    ci_stocks_separation: str = ""
    ci_lead_manager: str = ""
    ci_address: str = ""
    ci_turnover: float = 0.0
    ci_before_corporate_tax: float = 0.0
    ci_net_profit: float = 0.0
    ci_capital: float = 0.0
    ci_largest_shareholder: str = ""
    ci_largest_shareholder_rate: float = 0.0
    ci_po_expected_price: str = ""
    ci_po_expected_stocks: int = 0
    ci_po_expected_amount: str = ""
    ci_listing_expected_stocks: int = 0
    ci_before_po_capital: float = 0.0
    ci_before_po_stocks: int = 0.0
    ci_after_po_capital: float = 0.0
    ci_after_po_stocks: int = 0.0
    ci_most_subscription: str = ""
    ci_big_ir_plan: str = ""
    ci_demand_forecast_date: str = ""
    ci_public_subscription_date: str = ""
    ci_refund_date: str = ""
    ci_payment_date: str = ""
    ci_listing_date: str = ""
    ci_hope_po_price: str = ""
    ci_hope_po_amount: str = ""
    ci_confirm_po_price: int = 0
    ci_confirm_po_amount: float = 0.0
    ci_subscription_warrant_money_rate: str = ""
    ci_subscription_competition_rate: str = ""
    ci_public_offering_stocks: str = ""
    ci_professional_investor_stock: int = 0
    ci_professional_investor_rate: int = 0
    ci_esa_stock: int = 0
    ci_esa_rate: int = 0
    ci_general_subscriber_stock: int = 0
    ci_general_subscriber_rate: int = 0
    ci_overseas_investor_stock: int = 0
    ci_overseas_investor_rate: int = 0
    ci_noted_items_check: str = ""
    ci_guidelines_check: str = ""
    ci_small_ir_plan: str = ""
    ci_receipt_way: str = ""
    ci_receipt_place: str = ""
    ci_ask_tel: str = ""
    ci_organizer_homepage: str = ""
    ci_most_quantity: int = 0
    ci_unit: str = ""
    ci_competition_rate: str = ""
    ci_current_ratio: int = 0
    ci_like: int = 0
    ci_dislike: int = 0
    ci_vitalization1: str = "Y"
    ci_vitalization2: str = "Y"
    ci_vitalization3: str = "Y"
    ci_vitalization4: str = "Y"
    ci_vitalization5: str = "Y"
    ci_vitalization6: str = "Y"
    ci_demand_schedule: str = "Y"
    ci_demand_schedule_state: str = State.UPLOAD.value
    ci_demand_schedule_datetime: datetime = datetime.now()
    ci_demand_result: str = "Y"
    ci_demand_result_state: str = State.UPLOAD.value
    ci_demand_result_datetime: datetime = datetime.now()
    ci_public_schedule: str = "Y"
    ci_public_schedule_state: str = State.UPLOAD.value
    ci_public_schedule_datetime: datetime = datetime.now()
    ci_datetime: datetime = datetime.now()


class GeneralCreateSchema(GeneralBase):
    @validator("ci_code", pre=True)
    def validate_ci_code(cls, value):
        value = value.replace(" ", "").strip()
        return value

    @validator("ci_face_value", pre=True)
    def validate_ci_face_value(cls, value):
        if isinstance(value, str):
            if value.isnumeric():
                value = int(value)
                return value
            else:
                value = value.replace("원", "").strip()
                return int(value)
        return None

    @validator("ci_market_separation", pre=True)
    def validate_ci_market_separation(cls, value):
        return converters.extensions_to_string(value)

    @validator("ci_list_type", pre=True)
    def validate_ci_list_type(cls, value):
        value = converters.extensions_to_string(value)
        value = converters.ci_list_type(value)
        return value

    @validator("ci_review_c_date", pre=True)
    def convert_ci_review_c_date(cls, value):
        return value.replace(" ", "").replace(".", "/").replace("-", "/").strip()

    @validator("ci_review_a_date", pre=True)
    def convert_ci_review_a_date(cls, value):
        return value.replace(" ", "").replace(".", "/").replace("-", "/").strip()

    @validator("ci_establishment_date", pre=True)
    def convert_ci_establishment_date(cls, value):
        return converters.dot_dash_to_slash(value)

    @validator("ci_settlement_month", pre=True)
    def convert_ci_settlement_month(cls, value):
        return converters.only_digits_to_int(value)

    @validator("ci_worker_cnt", pre=True)
    def convert_ci_worker_cnt(cls, value):
        return converters.only_digits_to_int(value)

    @validator("ci_turnover", pre=True)
    def convert_ci_turnover(cls, value):
        return converters.change_currency(value)

    @validator("ci_before_corporate_tax", pre=True)
    def convert_ci_before_corporate_tax(cls, value):
        return converters.change_currency(value)

    @validator("ci_net_profit", pre=True)
    def convert_ci_net_profit(cls, value):
        return converters.change_currency(value)

    @validator("ci_capital", pre=True)
    def convert_ci_capital(cls, value):
        return converters.change_currency(value)

    @validator("ci_largest_shareholder_rate", pre=True)
    def convert_ci_largest_shareholder_rate(cls, value):
        return converters.string_rate_to_percentage(value)

    @validator("ci_po_expected_amount", pre=True)
    def convert_ci_po_expected_amount(cls, value):
        return converters.ci_po_expected_amount(value)

    @validator("ci_listing_expected_stocks", pre=True)
    def convert_ci_listing_expected_stocks(cls, value):
        result = converters.only_digits(value)
        if result is None or result in string.whitespace:
            return 0
        result = result.strip()
        return int(result)

    @validator("ci_before_po_capital", pre=True)
    def conver_before_po_capital(cls, value):
        return converters.string_capital_to_float(value)

    @validator("ci_after_po_capital", pre=True)
    def conver_after_capital_to_int(cls, value):
        return converters.string_capital_to_float(value)

    @validator("ci_before_po_stocks", pre=True)
    def conver_before_po_stocks(cls, value):
        return converters.string_stocks_to_int(value)

    @validator("ci_after_po_stocks", pre=True)
    def conver_after_po_stocks(cls, value):
        return converters.string_stocks_to_int(value)

    @validator("ci_lead_manager", pre=True)
    def convert_ci_lead_manager(cls, value):
        return converters.none_to_empty_string(value)

    @validator("ci_homepage")
    def convert_ci_homepage(cls, value):
        value = converters.none_to_empty_string(value)
        value = converters.cleaning_ci_homepage(value)
        return value

    @validator("ci_big_ir_plan", pre=True)
    def convert_ci_big_ir_plan(cls, value):
        value = value.strip()
        return value

    @validator("ci_confirm_po_price", pre=True)
    def convert_ci_confirm_po_price(cls, value):
        if isinstance(value, str):
            return int(converters.only_digits(value))
        return value

    @validator("ci_confirm_po_amount", pre=True)
    def convert_ci_confirm_po_amount(cls, value):
        if isinstance(value, str):
            return float(converters.only_digits(value))
        return value

    @validator("ci_professional_investor_stock", pre=True)
    def convert_ci_professional_investor_stock(cls, value):
        if isinstance(value, int):
            return value
        value = int(converters.only_digits(value))
        return value

    @validator("ci_professional_investor_rate", pre=True)
    def convert_ci_professional_investor_rate(cls, value):
        if isinstance(value, int):
            return value
        value = value.split("%")[0].replace(".", "").strip()
        return int(value)

    @validator("ci_esa_stock", pre=True)
    def convert_ci_esa_stock(cls, value):
        if isinstance(value, int):
            return value
        value = int(converters.only_digits(value))
        return value

    @validator("ci_esa_rate", pre=True)
    def convert_ci_esa_rate(cls, value):
        if isinstance(value, int):
            return value
        value = value.split("%")[0].strip().replace(" ", "").replace(".", "")
        return int(value)

    @validator("ci_general_subscriber_stock", pre=True)
    def convert_ci_general_subscriber_stock(cls, value):
        if isinstance(value, int):
            return value
        value = int(converters.only_digits(value))
        return value

    @validator("ci_general_subscriber_rate", pre=True)
    def convert_ci_general_subscriber_rate(cls, value):
        if isinstance(value, int):
            return value
        value = value.strip().replace(".", "").replace(" ", "").split("%")[0]
        return int(value)

    @validator("ci_overseas_investor_stock", pre=True)
    def convert_ci_overseas_investor_stock(cls, value):
        if isinstance(value, int):
            return value
        value = int(converters.only_digits(value))
        return value

    @validator("ci_overseas_investor_rate", pre=True)
    def convert_ci_overseas_investor_rate(cls, value):
        if isinstance(value, int):
            return value
        value = value.strip().replace(" ", "").replace(".", "").split("%")[0]
        return int(value)

    @validator("ci_hope_po_price", pre=True)
    def convert_ci_hope_po_price(cls, value):
        string_value = converters.range_of_digits(value)
        value = string_value.strip().replace(" ", "")
        return value

    @validator("ci_hope_po_amount", pre=True)
    def convert_ci_hope_po_amount(cls, value):
        string_value = converters.range_of_digits(value)
        value = string_value.strip().replace(" ", "")
        return value

    @validator("ci_subscription_competition_rate", pre=True)
    def convert_ci_subscription_competition_rate(cls, value):
        result = value.strip().replace("대", ":")
        return result

    @validator("ci_subscription_warrant_money_rate", pre=True)
    def convert_ci_subscription_warrant_money_rate(cls, value):
        result = value.strip()
        return result

    @validator("ci_listing_date", pre=True)
    def convert_ci_listing_date(cls, value):

        result = converters.dot_dash_to_slash(value)
        return result

    @validator("ci_payment_date", pre=True)
    def convert_ci_payment_date(cls, value):
        result = converters.dot_dash_to_slash(value)
        return result

    @validator("ci_refund_date", pre=True)
    def convert_ci_refund_date(cls, value):
        result = converters.dot_dash_to_slash(value)
        return result

    @validator("ci_public_subscription_date", pre=True)
    def convert_ci_public_subscription_date(cls, value):
        result = converters.add_year_in_date_or_not(value)
        return result

    @validator("ci_demand_forecast_date", pre=True)
    def convert_ci_demand_forecast_date(cls, value):
        result = converters.add_year_in_date_or_not(value)
        return result

    @validator("ci_competition_rate", pre=True)
    def convert_ci_competition_rate(cls, value):
        return value

    @validator("ci_po_expected_price", pre=True)
    def convert_ci_po_expected_price(cls, value):
        return ""

    @validator("ci_po_expected_stocks", pre=True)
    def convert_ci_po_expected_stocks(cls, value):
        return converters.only_digits_to_int(value)
