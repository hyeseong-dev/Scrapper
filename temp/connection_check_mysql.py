import pymysql
from config.settings import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)


# Connect to the MySQL server
connection = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
)

# Check the connection
try:
    with connection.cursor() as cursor:
        # Execute a simple SQL statement to check the connection
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Connection successful, result:", result)
finally:
    # Close the connection
    connection.close()
