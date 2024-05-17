# Homework
This project demonstrates the implementation of a Flask server 
with two API endpoints and a Flask client with database integration. 
The Flask client retrieves data from the server, parses it, 
and stores it in a SQLite database. Additionally, the client
can send POST requests to the server. Docker file was 
created later.


## Prerequisites

* Python 3.10
* Flask
* requests
* sqlite3

## Setup Instructions

### Server Setup

1. Install the required packages
`pip install -r requirements.txt`
2. Run the Flask server:
`Flask run`

### Client Setup

1. Install the required packages
`pip install -r requirements.txt`
2. Run the Flask client:
`python client.py`

## API Endpoints

### Server Endpoints

#### GET

* GET /api/v2/get/data
* Description: Retrieves data from the server.
* URL: http://localhost:5000/api/v2/get/data
* Method: GET
* Response: JSON data from sample.json.

#### POST

* POST /api/v2/add/data
* Description: Adds data to the server.
* URL: http://localhost:5000/api/v2/add/data
* Method: POST
* Request Body: JSON data to be stored in sample.json.
* Response: Status message confirming receipt of data.

### Client Functions

#### post_request()

* Description: Sends JSON data from newsample.json to the server.
* Endpoint: http://localhost:5000/api/v2/add/data
* Method: POST
* Response: Status message confirming successful data submission.

#### get_request()

* Description: Retrieves JSON data from the server, parses it.
* Endpoint: http://localhost:5000/api/v2/get/data
* Method: GET
* Response: Status message confirming data retrieval and storage.

## Parser Implementation

* parser.py:
* JSONParser class for parsing JSON data.
* JSONListParser class for parsing a list of student data.
* Student class representing a student entity.

## Dockerfile Confirguration

* Dockerfile


```FROM python:3.10-slim

FROM python:3.10-slim


WORKDIR /C:/Users/Tamerlan/Desktop/homework


COPY requirements.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 7000


CMD [ "python3", "-m" , "flask", "run"]
```




Running The Project with Docker

1. Build the Docker Image:
`docker build -t my_flask_app`. 
2. Run the Docker container:
`docker run -p 7000:5000 flask-client-server`


