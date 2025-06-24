FROM python:3.10.18

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]