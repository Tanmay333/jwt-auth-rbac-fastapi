from mongoengine import Document, StringField, EnumField
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(Document):
    username = StringField(required=True, unique=True)
    hashed_password = StringField(required=True)
    role = EnumField(UserRole, default=UserRole.USER)

    meta = {'collection': 'users'}