ALTER TABLE
    trustinv.company_info_prediction MODIFY COLUMN ci_participation BIGINT(20);

ALTER TABLE
    trustinv.company_info_general MODIFY COLUMN ci_idx INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE
    trustinv.company_info_financial MODIFY COLUMN cif_idx INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE
    trustinv.company_info_prediction MODIFY COLUMN cip_idx INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE
    trustinv.company_info_shareholder MODIFY COLUMN cis_idx INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE
    trustinv.company_info_subscriber MODIFY COLUMN cis_idx INT AUTO_INCREMENT PRIMARY KEY;

-- 기존 B디비의 데이터가 들어 있는 테이블을 A디비에 새로 생성함.

-- create table test_trustinv.company_info_general as select * from trustinv.company_info_general;

-- create table test_trustinv.company_info_financial as select * from trustinv.company_info_financial;

-- create table test_trustinv.company_info_prediction as select * from trustinv.company_info_prediction;

-- create table test_trustinv.company_info_shareholder as select * from trustinv.company_info_shareholder;

-- create table test_trustinv.company_info_subscriber as select * from trustinv.company_info_subscriber;

-- 테이블 데이터 개수

-- select count(*) from test_trustinv.company_info_general ;

-- select count(*) from test_trustinv.company_info_financial ;

-- select count(*) from test_trustinv.company_info_prediction ;

-- select count(*) from test_trustinv.company_info_shareholder ;

-- select count(*) from test_trustinv.company_info_subscriber ;

-- - truncate test_trustinv tables

select count(*) from trustinv.app_calendar ;

select count(*) from trustinv.company_info_general ;

select count(*) from trustinv.company_info_financial ;

select count(*) from trustinv.company_info_prediction ;

select count(*) from trustinv.company_info_shareholder ;

select count(*) from trustinv.company_info_subscriber ;

---

select count(*) from test_trustinv.app_calendar ;

select count(*) from test_trustinv.company_info_general ;

select count(*) from test_trustinv.company_info_financial ;

select count(*) from test_trustinv.company_info_prediction ;

select count(*) from test_trustinv.company_info_shareholder ;

select count(*) from test_trustinv.company_info_subscriber ;

select * from test_trustinv.app_calendar ;

select * from test_trustinv.company_info_general ;

select * from test_trustinv.company_info_financial ;

select * from test_trustinv.company_info_prediction ;

select * from test_trustinv.company_info_shareholder ;

select * from test_trustinv.company_info_subscriber ;

truncate table test_trustinv.app_calendar ;

truncate table test_trustinv.company_info_general ;

truncate table test_trustinv.company_info_financial ;

truncate table test_trustinv.company_info_prediction ;

truncate table test_trustinv.company_info_shareholder ;

truncate table test_trustinv.company_info_subscriber ;

truncate table trustinv.app_calendar ;

truncate table trustinv.company_info_general ;

truncate table trustinv.company_info_financial ;

truncate table trustinv.company_info_prediction ;

truncate table trustinv.company_info_shareholder ;

truncate table trustinv.company_info_subscriber ;

select *
from
    test_trustinv.company_info_general
where ci_name = '오브젠';

select
    ci_demand_forecast_date,
    ci_public_subscription_date,
    ci_refund_date,
    ci_payment_date,
    ci_listing_date
from company_info_general;

select *
from app_calendar
where (
        256,
        257,
        258,
        259,
        260,
        261,
        262,
        263,
        264,
        265,
        266,
        267
    ) in ci_idx;