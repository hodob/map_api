DROP DATABASE map_api WITH (FORCE);
CREATE DATABASE map_api
    WITH
    OWNER = waterdats
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


UPDATE public.api_user_user SET is_staff=true WHERE id=1;
select  * from public.api_user_user ;




CREATE VIEW 현재장비 (성명, 전화번호)
AS SELECT 성명 전화번호
FROM 고객
WHERE 주소 = '서울시';

select distinct id from inu_obs_mi iom;
select * from inu_obs_mi ;
select * from inu_obs_mi LIMIT 100;
select id from inu_obs_mi GROUP by id; 

select * from inu_obs_mi iom where temp in (select temp from inu_obs_mi iom where temp='28' or temp = '28.1' group by temp);
select temp from inu_obs_mi iom where temp='28' or temp = '28.1' group by temp;
select * from inu_obs_mi order by obs_time  DESC limit 100;
select id ,max(obs_time) from inu_obs_mi group by id ;

select * from inu_obs_mi where (id, obs_time) in (select id ,max(obs_time) from inu_obs_mi);
select * from inu_obs_mi where id = 866642054441003;

select id 장비번호 ,max(obs_time) 날짜 ,pow , temp , mb, mb_std , delta , vi_time , inu_depth  from inu_obs_mi group by id ;

