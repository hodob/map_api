DROP DATABASE db_name WITH (FORCE);
CREATE DATABASE map_api
    WITH
    OWNER = waterdats
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    