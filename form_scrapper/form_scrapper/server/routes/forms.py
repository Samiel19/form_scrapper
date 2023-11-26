from urllib import parse as urlparse

from core.form_maker import find_document, insert_document
from fastapi import APIRouter
from form_scrapper.server.database import forms_collection

router = APIRouter()


@router.post("/get_form", response_description="Best template for you data")
def get_template_data(form):
    form = dict(urlparse.parse_qsl(form))
    template = find_document(forms_collection, form)
    return template


@router.post("/post_template", response_description="Make form teplate")
def post_template_data(data):
    new_form = dict(urlparse.parse_qsl(data))
    insert_document(forms_collection, new_form)
    return "New form template added!"
