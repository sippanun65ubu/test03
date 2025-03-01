FROM python:3.11

WORKDIR /webproj

COPY . .

RUN pip install django

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py" , "runserver"]