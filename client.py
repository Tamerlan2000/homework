import requests
import json
import sqlite3
from parser import JSONListParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from parser_one import Base, Parser

# DATABASE_URL = 'sqlite:///my_database.db'
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# Base.metadata.create_all(engine)

def post_request():
    url = 'http://localhost:7000/api/v2/add/data'
    with open('new_sample.json') as file:
        json_object = json.load(file)

    response = requests.post(url, json=json_object)
    if response.status_code == 200:
        print('JSON data sent successfully!')
    else:
        print('Failed to send JSON data:', response.status_code)


def get_request(session):

    # url = 'http://localhost:7000/api/v2/get/data'
    # response = requests.get

    response = requests.get('http://localhost:7000/api/v2/get/data')
    #response_json = response.text


    if response.status_code == 200:
        # try:
        res = Parser(response.text)
        print('Object created')
        parsed_data = res.parse_json()
        print('Parsed data')
        session.add(parsed_data)
        print('Added tables to database')
        session.commit()
        # except Exception:
        #     print('Error is here:')
        #     #session.rollback()# New change
        #     print(Exception)

    else:
        print('Failed to get data:', response.status_code)

user_questionary = '''
Choose your action:
1. GET option request
2. POST option request
3. EXIT
Selected option: '''


if __name__ == '__main__':
    DATABASE_URL = 'sqlite:///my_database.db'

    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    while True:
        user_option = input(user_questionary)
        match user_option:
            case '1':
                print('GET')
                get_request(session)
            case '2':
                post_request()
            case '3':
                print('Exiting client')
                session.close()
                engine.dispose()
                break
