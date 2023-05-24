FROM python:alpine

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

CMD ["python", "report.py"]
