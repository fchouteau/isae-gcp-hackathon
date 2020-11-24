FROM python:3.8
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app/
ENV TORCH_HOME="/app/"

COPY app.py /app/
COPY preload.py /app/
RUN python /app/preload.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
