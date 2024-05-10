import psycopg2
import requests
from parser import JSONParser
import json

response = requests.get('http://example.com/api/v2/get/data')

try:
    response.raise_for_status()  # Raise an exception for bad status codes
    json_data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON data. Response may not be valid JSON.")
    json_data = {}

parser = JSONParser(json_data)
parsed_data = parser.parse()

print('Data gathered, parsed, and stored in the database.')

# Assuming you have a function to establish a database connection
def get_db_connection():
    try:
        return psycopg2.connect(
            host='your_database_host',
            database='your_database_name',
            user='your_database_user',
            password='your_database_password'
        )
    except psycopg2.OperationalError as e:
        print(f'Error connecting to the database: {e}')
        exit(1)

# Database storage logic
try:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO your_table_name (message) VALUES (%s)", (parsed_data,))
    conn.commit()
    cur.close()
    conn.close()
    print('Data stored in the database.')
except Exception as e:
    print(f'Error storing data in the database: {str(e)}')
