# This sets up the container with Python 3.10 installed.
FROM python:3.10

COPY . /Bot

WORKDIR /Bot

RUN pip install -r requirements.txt

EXPOSE 5000


RUN mkdir ~/.Bot


ENTRYPOINT ["taipy", "run"]

CMD ["main.py"]