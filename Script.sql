DROP DATABASE map_api WITH (FORCE);
CREATE DATABASE map_api
    WITH
    OWNER = waterdats
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    