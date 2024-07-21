FROM python:3.11

COPY . .

RUN source ./venv/bin/activate
#RUN pip install -r requirements.txt

# uvicorn main:main --reload --host 0.0.0.0 --port 8000
CMD ["uvicorn", "main:main", "--reload", "--host", "0.0.0.0", "--port", "8000"]