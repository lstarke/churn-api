from marshmallow import Schema, fields

class ChurnSchema(Schema):
    tenure = fields.Int(required=True)
    OnlineSecurity = fields.Str(required=True)
    TechSupport = fields.Str(required=True)    
    Contract = fields.Str(required=True)
    tenure_description = fields.Str(required=True)