from marshmallow import Schema, fields
from marshmallow.validate import Email

class LoginSchema(Schema):
    email = fields.Email(required = True)
    password = fields.Str(requird=True)