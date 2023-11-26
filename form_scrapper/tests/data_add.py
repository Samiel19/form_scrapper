from form_scrapper.server.database import forms_collection


def insert_document(collection, data):
    """Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


new_form = {
    "name": "form_name2",
    "order_email": "email",
    "order_phone": "phone",
    "order_date": "date",
}

new_form_2 = {
    "name": "form_name2",
    "order_email": "email",
    "phone": "phone",
    "order_date": "date",
}


# FOR TESTING OUTSIDE DOCKER CONTAINER
insert_document(forms_collection, new_form)
insert_document(forms_collection, new_form_2)
