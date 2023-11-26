# FormScrapperApp
App for scrapping forms


## API (server part) for form template search

This service is designed for searching best template for forms in NOSQL DB. The search fields are email, phone, date and text. Phone, date and email have validation.


[github](https://github.com/Samiel19)

## Technology stack
The following technologies were used in the development of this application:

- Python 3.11

- FastAPI

- MongoDB

- Docker

- Poetry


## Project functionality

The user can add form templates at andpoint "/forms/post_template" and after this post search data
at endpoint "/forms/get_form" and get best form template for his form.
At endpoint "/forms/templates" user can get all templates.

For example: if you have

new_form = {
    "name": "form_name2",
    "order_email": "email",
    "order_phone": "phone",
    "order_date": "date",
}

AND

new_form_2 = {
    "name": "form_name2",
    "order_email": "email",
    "phone": "phone",
    "order_date": "date",
}

you can get post your form data as "order_email=test@test.com&phone=%2B7 999 999 99 99"
and get "new_form_2" as best form template.

If there is no template with at least one same pair "field-value" you will have
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE,
    ...
}

as answer.


# Infrastructure

        1. The project works with the MongoDB.

        2. The project is hosted in two Docker containers:
            MongoDB and form_scrapper.


# Testing and deploy

   For deploy:

   - Fork this repo

   - Install Docker

   - Go to directory with test_script.sh "cd form_scrapper/form_scrapper/"

   - Run "bash test_script.sh"

   The script with make and run containers with scrapper and db, make contaners network.
   If you already have this containers, script will destroy containers and network.
   After this, script will make three form templates while sending data:

    "name=form_name3&order_email=email&phone=phone&order_date=date"
    "name=form_name2&order_email=email&order_phone=phone&order_date=date"
    "name=form_name&email=email&phone=phone&date=date"

   Then, script make requests to get best templates four times. One for each template and one with no template.
   After this you will see all form templates in db.

   - Also, you can use "http://localhost:8000/docs#/" to test app with another data.

   In this case you will post data in form "f_name1=value1&f_name2=value2". And don't use "+", only %2B.


# Code formatting

        Code corresponds PEP8.
