import pandas as pd 
import numpy as np

from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= [ "date", "amount","category", "description"])
            df.to_csv(cls.CSV_FILE, index= False)
    @classmethod
    def add_entry(cls, date, amount, category, descriptions):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "descriptions":descriptions
        }
CSV.initialize_csv()            








