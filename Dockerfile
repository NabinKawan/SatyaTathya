FROM python:3.10
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./main.py /code
COPY ./server /code/server
EXPOSE 80
CMD ["python","main.py" ]