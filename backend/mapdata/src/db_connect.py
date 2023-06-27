
import psycopg2 as psycopg
import environ
env = environ.Env()
class DatabaseConnection:

    def __init__(self):
        self.conn = psycopg.connect(
            host=env('DATABASE_HOST'),
            dbname=env('DATABASE_NAME2'),
            user=env('DATABASE_USER'),
            password=env('DATABASE_PASSWORD'),
            port="5432"
        )

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


