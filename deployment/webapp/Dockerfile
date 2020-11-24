FROM python:3.8
WORKDIR /app/

RUN pip install flask jinja2

COPY . /app/

EXPOSE 8000

CMD ["python", "/app/app.py"]
