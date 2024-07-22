import os
import mysql.connector
from dotenv import load_dotenv



load_dotenv()

DB_NAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DATABASE")

connection = mysql.connector.connect(
    user=DB_NAME,
    password=DB_PASSWORD,
    host= DB_HOST,
    database=DATABASE
)


cursor = connection.cursor()

queries = """CREATE TABLE IF NOT EXISTS software_class(
id int,
name varchar(50)
)"""

cursor.execute(queries)
connection.commit()
cursor.close()