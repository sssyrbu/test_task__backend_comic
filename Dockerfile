FROM python:3.11.8-alpine3.18

WORKDIR /comic_api

COPY . /comic_api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["sh", "-c", "cd app/ && pytest tests/ && python3 main.py"]