FROM python:3.6
WORKDIR /app
COPY . /app
CMD["python3","script.py"]