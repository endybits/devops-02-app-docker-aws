FROM python:3.9

WORKDIR /app

COPY makefile /app/
COPY requirements.txt /app/requirements.txt
COPY . /app/app

RUN make install

EXPOSE 80

CMD [ "python3", "app/main.py" ]