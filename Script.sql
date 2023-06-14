DROP DATABASE map_api WITH (FORCE);
CREATE DATABASE map_api
    WITH
    OWNER = waterdats
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


UPDATE public.api_user_user SET is_staff=true WHERE id=1;
select  * from public.api_user_user ;
