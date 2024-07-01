import os
import psycopg2
import pandas as pd
from config import Config

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        )
        self.cursor = self.connection.cursor()

    def check_table_exists(self, table_name):
        query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = '{table_name}'
        );
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def create_table_from_sql(self, table_name):
        sql_path = os.path.join(os.path.dirname(__file__), 'sql', f'{table_name}.sql')
        with open(sql_path, 'r') as file:
            create_table_query = file.read()
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def bulk_insert(self, df: pd.DataFrame, table_name, columns):
        # Convert DataFrame to list of tuples
        tuples = [tuple(x) for x in df.to_numpy()]
        # Join the columns into a comma-separated string
        columns_str = ','.join(columns)
        # Create the INSERT query string with placeholders
        placeholders = ','.join(['%s'] * len(columns))
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
        # Execute the insert query with the list of tuples
        self.cursor.executemany(insert_query, tuples)
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
