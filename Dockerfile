FROM python:3.10.9-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
