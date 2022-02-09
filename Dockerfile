FROM python:3.9

EXPOSE 8000

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py test
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
