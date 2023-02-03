from typing import Type, Union
import datetime
from sqlalchemy import Column, DateTime, Float, String, Text, text, ForeignKey, SMALLINT
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class CompanyInfoGeneral(Base):
    __tablename__ = "company_info_general"
    __table_args__ = {"comment": "기업정보 기본"}

    ci_idx: int = Column(INTEGER(11), primary_key=True, autoincrement=True)

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

    company = relationship("CompanyInfoGeneral", back_populates="app_calendars")
