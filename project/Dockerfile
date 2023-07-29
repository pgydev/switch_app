
FROM python:3.9-slim


WORKDIR /app


COPY . /app/



RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


CMD "cd" "project"; "gunicorn" "-w"  "4" "main:create_app" "--bind" "0.0.0.0:8000"

