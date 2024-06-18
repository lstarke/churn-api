from marshmallow import Schema, fields

class ChurnSchema(Schema):
    tenure = fields.Int(required=True)
    online_security = fields.Bool(required=True)
    tech_support = fields.Bool(required=True)    
    contract = fields.Str(required=True)