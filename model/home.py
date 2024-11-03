from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Int(required=True)
user_schema = UserSchema()
