FROM python:3.12-slim

WORKDIR /maksymenko

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "gtrans3_demo.py"]