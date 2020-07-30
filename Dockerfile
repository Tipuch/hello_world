FROM python:3.8
WORKDIR /vagrant
EXPOSE 8000
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONPATH=/vagrant
COPY . .
CMD python manage.py runserver 0.0.0.0:8000