#!/bin/sh


docker stop form_scrapper && docker rm form_scrapper
docker stop mongodb && docker rm mongodb
docker network rm form-network
docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server
docker build -t form_scrapper .
docker run -d --name form_scrapper -p 8000:8000 form_scrapper
docker network create form-network
docker network connect form-network mongodb
docker network connect form-network form_scrapper

sleep 1
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/post_template?data=name%3Dform_name%26email%3Demail%26phone%3Dphone%26date%3Ddate' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/post_template?data=name%3Dform_name2%26order_email%3Demail%26order_phone%3Dphone%26order_date%3Ddate' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/post_template?data=name%3Dform_name3%26order_email%3Demail%26phone%3Dphone%26order_date%3Ddate' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/get_form?form=order_email%3Demail%40email.com%26phone%3D%252B7%20999%20999%2099%2099' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/get_form?form=email%3Demail%40email.com%26phone%3D%252B7%20999%20999%2099%2099' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/get_form?form=order_email%3Demail%40email.com%26order_phone%3D%252B7%20999%20999%2099%2099' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'POST' \
  'http://localhost:8000/forms/get_form?form=orderemail%3Demail%40email.com%26orderphone%3D%252B7%20999%20999%2099%2099' \
  -H 'accept: application/json' \
  -d ''

sleep .5
echo -en '\n'

curl -X 'GET' \
  'http://localhost:8000/forms/templates' \
  -H 'accept: application/json'
