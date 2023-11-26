import pymongo

client = pymongo.MongoClient("mongodb://mongodb")
db = client["form_scrapper"]
forms_collection = db["forms"]


def retrieve_forms():
    forms = []
    template = forms_collection.find()
    for form in template:
        form["_id"] = str(form["_id"])
        forms.append(form)
    return forms
