# Import the required modules
import time
import time
from mapdata.src.db_connect import DatabaseConnection


class DatabaseQuery:
    def __init__(self):
        pass

    # "select * from inu_obs_mi where (id, obs_time) in (select id ,max(obs_time) from inu_obs_mi group by id)")
    def getallmapdata(self):
        with DatabaseConnection() as db_conn:
            cur = db_conn.cursor()
            select_data = str(
                "select * from inu_obs_mi where (id, obs_time) in ("
                "select id, max(obs_time) from inu_obs_mi group by id)"
            )
            cur.execute(select_data)
            cached_data = cur.fetchall()
            cur.close()

        return cached_data
    def getallmapdata2(self):
        global cached_data, last_updated_time, cache_expiry_time
        current_time = time.time()
        if current_time - last_updated_time > cache_expiry_time:
            with DatabaseConnection() as db_conn:
                cur = db_conn.cursor()
                select_data = str(
                    "select * from inu_obs_mi where (id, obs_time) in ("
                    "select id, max(obs_time) from inu_obs_mi group by id)"
                )
                cur.execute(select_data)
                cached_data = cur.fetchall()
                cur.close()

            last_updated_time = current_time
        return cached_data

    def getallmapdata3(self):
        with DatabaseConnection() as db_conn:
            cur = db_conn.cursor()
            select_data = str(
                "select * from inu_info"
            )
            cur.execute(select_data)
            fetched_data = cur.fetchall()
            cur.close()
        transformed_data = []
        for row in fetched_data:
            inu_id = row[0]
            latitude = row[2]
            longitude = row[3]
            transformed_data.append({"title":inu_id,"latlng": {"lat":latitude,"lng":longitude}})

        return transformed_data


    # def getallmapdata(self):

    #
    #     # Check if the cache is expired
    #     if current_time - last_updated_time > cache_expiry_time:
    #         # Cache is expired, update the data
    #         cur =db_conn.cursor()
    #         select_data = str("select * from inu_obs_mi where (id, obs_time) in (select id ,max(obs_time) from inu_obs_mi group by id)")
    #         cur.execute(select_data)
    #         cached_data = cur.fetchall()
    #         cur.close()
    #
    #
    #         last_updated_time = current_time
    #
    #     return cached_data





# def getallmapdata():
#     global cached_data, last_updated_time
#
#     current_time = time.time()
#
#     # Check if the cache is expired
#     if current_time - last_updated_time > cache_expiry_time:
#         # Cache is expired, update the data
#         conn = get_database_connection()
#         cur = conn.cursor()
#         select_data = str("select * from inu_obs_mi where (id, obs_time) in (select id ,max(obs_time) from inu_obs_mi group by id)")
#         cur.execute(select_data)
#         cached_data = cur.fetchall()
#         cur.close()
#         conn.close()
#
#         last_updated_time = current_time
#
#     return cached_data

# def list(self, request):
#     data = get_cached_data()
#     return Response(data)