FROM python:2.7.12

RUN mkdir -p /data/web

COPY requirements.txt /data/
COPY web/ /data/web/

RUN pip install -r /data/requirements.txt

WORKDIR /data/web/

ENTRYPOINT ["python", "/data/web/app.py"]
