FROM python:3.9

WORKDIR /app
ADD requirements.txt .
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y default-jdk
RUN pip install -U pip wheel cmake
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# RUN pip install --user -r requirements.txt
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000