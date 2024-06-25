from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import ChurnSchema
import pandas as pd
import numpy as np
import util

blp = Blueprint("Churn",  __name__, description="Churn predictions")

@blp.route("/churn")
class Churn(MethodView):
    
    def get(self):
        return "Hello Churn!"

    @blp.arguments(ChurnSchema)
    @blp.response(200)
    def post(self, churn_data):        
        input_df = pd.DataFrame(churn_data, index=[0])  

        preprocessor = util.get_preprocessor()
        preprocessed_df = preprocessor.transform(input_df)

        # resgatando a features categóricas
        enc_cat_features = preprocessor\
                   .named_transformers_["onehotencoder"]\
                   .get_feature_names_out()

        # resgatando a fetures numéricas
        enc_num_features = preprocessor\
                   .named_transformers_["minmaxscaler"]\
                   .get_feature_names_out()

        # concatenando os nomes da colunas
        labels = np.concatenate([enc_num_features, enc_cat_features])
        transformed_df_columns = pd.DataFrame(preprocessed_df, columns=labels)   
        response = transformed_df_columns[util.get_feature_names()]

        model = util.get_model()
        prediction = model.predict(response.values).tolist()[0]
        return jsonify(churn=prediction)

@blp.route("/churn/features")        
class ChurnFeatures(MethodView):
    def get(self):
        return jsonify(features=util.get_feature_names().tolist())
        