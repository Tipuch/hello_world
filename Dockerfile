FROM python:3.8
WORKDIR /hello_world
EXPOSE 8000
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONPATH=/hello_world
COPY . .
CMD python manage.py runserver 0.0.0.0:8000