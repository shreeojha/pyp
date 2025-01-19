FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r pyreq.txt
EXPOSE 7000
CMD ["python","app.py"]
