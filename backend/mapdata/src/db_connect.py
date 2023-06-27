
import psycopg2 as psycopg
import environ
env = environ.Env()

def get_database_connection():
    conn = psycopg.connect(
        host=env('DATABASE_HOST'),
        dbname=env('DATABASE_NAME'),
        user=env('DATABASE_USER'),
        password=env('DATABASE_PASSWORD'),
        port="5432"
    )
    return conn