import pymongo


client = pymongo.MongoClient('mongodb://mongodb')
db = client['form_scrapper']
forms_collection = db['forms']


async def retrieve_forms():
    forms = []
    async for form in forms_collection.find():
        forms.append(form)
    return forms