FROM python:3.9-slim
ADD . /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]