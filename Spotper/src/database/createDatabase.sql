CREATE TABLESPACE  ts_primary LOCATION 'C:\Users\User\Desktop\SportPerData\tablespaces\primary';

CREATE TABLESPACE  ts_secondary LOCATION 'C:\Users\User\Desktop\SportPerData\tablespaces\secondary';

CREATE TABLESPACE ts_tertiary LOCATION  'C:\Users\User\Desktop\SportPerData\tablespaces\tertiary';

CREATE DATABASE SPOTPER
TABLESPACE ts_primary;