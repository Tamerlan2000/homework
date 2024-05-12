import psycopg2
import requests
import json
import sqlite3
from parser import JSONListParser


def get_db_connection():
    try:
        return sqlite3.connect(
            host='your_database_host',
            database='your_database_name',
            user='your_database_user',
            password='your_database_password'
        )
    except psycopg2.OperationalError as e:
        print(f'Error connecting to the database: {e}')
        exit(1)


def post_request():
    url = 'http://localhost:7000/api/v2/add/data'
    with open('sample.json', 'r') as file:
        json_object = json(file)

    response = requests.post(url, json=json_object)
    if response.status_code == 200:
        print('JSON data sent successfully!')
    else:
        print('Failed to send JSON data:', response.status_code)

def get_request():
    url = 'http://localhost:7000/api/v2/get/data'
    response = requests.get(url)
    print(response)
    resp_dict = response.json()

    students_list = JSONListParser(resp_dict["Students"])
    print(students_list)
    # try:
    #     conn = get_db_connection()
    #     cur = conn.cursor()
    #     cur.execute("INSERT INTO your_table_name (message) VALUES (%s)", (parsed_data,))
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #     print('Data stored in the database.')
    # except Exception as e:
    #     print(f'Error storing data in the database: {str(e)}')

user_questionary = '''
Choose your action:
1. GET option request
2. POST option request
3. EXIT
Selected option: '''



if __name__ == '__main__':
    print('Starting client')
    print('--------------')

    while True:
        user_option = input(user_questionary)
        match user_option:
            case '1':
                print('GET')
                get_request()
            case '2':
                post_request()
            case '3':
                print('Exiting client')
                break

