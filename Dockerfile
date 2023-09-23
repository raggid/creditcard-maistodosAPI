FROM python:3.11 as requirements-stage

WORKDIR /tmp
RUN pip install pipenv
COPY app/Pipfile .
COPY app/Pipfile.lock .
RUN pipenv requirements > requirements.txt


FROM python:3.11

EXPOSE 8000
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install python-creditcard

COPY app .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ] 