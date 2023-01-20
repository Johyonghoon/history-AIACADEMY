FROM python:3.9

WORKDIR /app
ADD requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# RUN pip install --user -r requirements.txt
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000