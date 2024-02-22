FROM python:3.10

COPY . /neotour

WORKDIR /neotour

RUN python3 -m venv .venv
SHELL ["/bin/bash", "-c"]
RUN source .venv/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
