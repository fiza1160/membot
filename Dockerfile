FROM python:3

WORKDIR /opt

COPY src /opt/app

RUN pip install -r /opt/app/requirements.txt

CMD ["python", "/opt/app/main.py"]