import re
from core import enums


def insert_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


def check_type(element):
    """ Function to check type of field.
    """
    if not isinstance(element, str):
        return type(element)
    if re.match(enums.Regex.EMAIL_PATTERN, element):
        return "email"
    elif re.match(enums.Regex.PHONE_PATTERN, element):
        return "phone"
    elif re.match(enums.Regex.DATE_PATTERN_DOT, element) or re.match(enums.Regex.DATE_PATTERN_DASH, element):
        return "date"
    else:
        return "text"


def find_document(collection, elements):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    results = []
    for key, value in elements.items():
        elements[key] = check_type(value)
    for template in collection.find():
        results.append(
            (template["name"], {
                key: template[key] for key in template if key in elements and template[key] == elements[key]
                })
            )
        if not list(results[-1][-1]):
            results.pop(-1)
    if not results:
        return elements
    result_template_len = 0
    result_template = ''
    for case in results:
        if len(case[-1]) > result_template_len:
            result_template_len = len(case[-1])
            result_template = case[0]
    return result_template
