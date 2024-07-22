FROM python:3.11

COPY . .

# RUN pip install -r requirements.txt

# uvicorn main:main --reload --host 0.0.0.0 --port 8000
# docker start 808d657e69fa
CMD ["uvicorn", "main:main", "--reload", "--host", "0.0.0.0", "--port", "8000"]