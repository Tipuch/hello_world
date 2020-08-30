FROM python:3.8
WORKDIR /vagrant
EXPOSE 8000
RUN pip install --upgrade pip && pip install poetry
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry install
ENV PYTHONPATH=/vagrant
COPY . .
CMD python manage.py runserver 0.0.0.0:8000