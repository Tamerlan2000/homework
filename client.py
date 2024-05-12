import psycopg2
import requests
import json
import sqlite3
from parser import JSONListParser


# def get_db_connection():
#     try:
#         return sqlite3.connect(
#             host='your_database_host',
#             database='your_database_name',
#             user='your_database_user',
#             password='your_database_password'
#         )
#         return sqlite3.connect('your_database_name.db')  # Adjust database name as needed
#     except sqlite3.Error as e:
#         print(f'Error connecting to the database: {e}')
#         exit(1)

def get_db_connection():
    try:
        return sqlite3.connect('My_Database.db')  # Adjust database name as needed
    except sqlite3.Error as e:
        print(f'Error connecting to the database: {e}')
        exit(1)




def post_request():
    url = 'http://localhost:7000/api/v2/add/data'
    with open('newsample.json') as file:
        json_object = json.load(file)

    response = requests.post(url, json=json_object)
    if response.status_code == 200:
        print('JSON data sent successfully!')
    else:
        print('Failed to send JSON data:', response.status_code)

def get_request(con, cur):
    url = 'http://localhost:7000/api/v2/get/data'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            #resp_dict = response.json()
            content = json.loads(response.text)
            students = JSONListParser(content["Students"])
            print(students)
            for student in students.student_list:
                properties = (
                    student.student_id,
                    student.name,
                    student.grade,
                    student.nationality,
                    student.major,
                    student.university
                            )
                print(properties)
                cur.execute("INSERT INTO our_students VALUES(?,?,?,?,?,?);", properties)
                con.commit()
        except:
            print('Response content:', response.text)
            #print(Exception)

    else:
        print('Failed to get data:', response.status_code)



# def get_request():
#     url = 'http://localhost:7000/api/v2/get/data'
#     response = requests.get(url)
#     print(response)
#     resp_dict = response.json()
#
#     students = JSONListParser(resp_dict["Students"])
#     print(students)
#     for i in students.student_list:
#         print(students)
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
    con = sqlite3.connect("My_database.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS our_students(
       student_ID INT PRIMARY KEY,
       name TEXT,
       grade TEXT,
       nationality TEXT,
       major TEXT,
       university TEXT);
    """)
    con.commit()
    while True:
        user_option = input(user_questionary)
        match user_option:
            case '1':
                print('GET')
                get_request(con, cur)
            case '2':
                post_request()
            case '3':
                print('Exiting client')
                con.close()
                break

