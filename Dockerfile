FROM python:3

WORKDIR /opt

COPY app /opt/app

RUN pip install -r /opt/app/requirements.txt

CMD ["python", "/opt/app/main.py"]