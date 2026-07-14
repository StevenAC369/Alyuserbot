import psycopg2
from config import *

try:
    # Connect to your postgres DB
    if DATABASE_URL_ACTIVE:
        conn = psycopg2.connect(DATABASE_URL)
    else:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
    )
    print("Database connection established successfully.")

    # Create tables
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS sudoers (user_id BIGINT PRIMARY KEY, name VARCHAR(255));")
    cursor.execute("CREATE TABLE IF NOT EXISTS super_sudoers (user_id BIGINT PRIMARY KEY, name VARCHAR(255));")
    conn.commit()
    if cursor.fetchall() != []:
        print("Tables created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()