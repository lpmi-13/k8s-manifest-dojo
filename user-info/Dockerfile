FROM python:3.10-slim

WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

COPY . /app

EXPOSE 8010

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8010", "app:app"]
