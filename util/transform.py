import pandas as pd

def tenure_description(tenure: int) -> str:
  if tenure >= 0 and tenure <= 12:
    return "up to 1 year"
  elif tenure > 12 and tenure <=60:
    return "greater than a year to 5 years"
  else:
    return "more than 5 years"