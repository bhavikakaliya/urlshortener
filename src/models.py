from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class URLs(Document):
    long_url = StringField(required = True)
    short_url = StringField(required = True, unique = True)
    created_at = DateTimeField(default = datetime.now())