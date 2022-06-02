FROM python:3.8-slim
COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app
CMD ["python", "start_flask.py"]