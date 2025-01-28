from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class Project(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'projects'}

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Project, self).save(*args, **kwargs)
