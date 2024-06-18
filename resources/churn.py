from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import ChurnSchema
from util import transform

blp = Blueprint("Churn",  __name__, description="Churn predictions")

@blp.route("/churn")
class Churn(MethodView):
    
    def get(self):
        return "Hello Churn!"

    @blp.arguments(ChurnSchema)
    @blp.response(200, ChurnSchema)
    def post(self, churn_data):
        print(churn_data)
        