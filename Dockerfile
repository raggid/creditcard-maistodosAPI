FROM python:3.11 as requirements-stage

WORKDIR /tmp
RUN pip install pipenv
COPY app/Pipfile .
COPY app/Pipfile.lock .
RUN pipenv requirements > requirements.txt


FROM python:3.11

EXPOSE 8000
WORKDIR /app
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install git+https://github.com/maistodos/python-creditcard.git@main

COPY app .
ENV PYTHONPATH=/app

CMD [ "sh", "prestart.sh" ] 