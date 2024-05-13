FROM python:3.10-slim


WORKDIR /C:/Users/Tamerlan/Desktop/homework


COPY requirements.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7000


CMD [ "python3", "-m" , "flask", "run"]