from joblib import load

def get_pipeline():
  return load("ml-models/churn-pipeline.joblib")

def get_model():
  return load("ml-models/xgb_model.joblib")

def get_feature_names():
  return load("ml-models/features.names")

def get_preprocessor():
  return load("ml-models/preprocessor.joblib")

