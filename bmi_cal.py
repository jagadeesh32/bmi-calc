import pandas as pd
import numpy as np


# Given BMI Table
min_range = 0
max_range = 50
bmi_table = [
    {"category": "Underweight", "range_min": min_range,
        "range_max": 18.4, "risk": "Malnutrition risk"},
    {"category": "Normal weight", "range_min": 18.5,
        "range_max": 24.9, "risk": "Low risk"},
    {"category": "Overweight", "range_min": 25,
        "range_max": 29.9, "risk": "Enhanced risk"},
    {"category": "Moderately obese", "range_min": 30,
        "range_max": 34.9, "risk": "Medium risk"},
    {"category": "Severely obese", "range_min": 35,
        "range_max": 39.9, "risk": "High risk"},
    {"category": "Very severely obese", "range_min": 40,
        "range_max": max_range, "risk": "Very high risk"},
]

# convert input to dataframe
bmi_table_df = pd.DataFrame(bmi_table)


class LoadJsonToDataFrame:
    def __init__(self, file):
        self.file = file
    
    def load_json(self):
        dataframe = pd.read_json(self.file)
              
        print(dataframe.head())
        return dataframe
    

class BMICalculator:
    def __init__(self, data):
        self.data = data
        self.result_index = 0
        self.result_list = []
        self.risk = None
        self.category = None

    def calculate_bmi(self):
        # Calcualte Given DataFrame BMI
        self.data["bmi"] = round(self.data['WeightKg'] / (self.data['HeightCm']/100) ** 2, 2)
        pass

    def calculate_risk(self):
        # Calcualte Given DataFrame BMI Risk
        self.data["risk"] = self.data["bmi"].apply(self.get_risk)
        pass

    def calculate_category(self):
        # Calcualte Given DataFrame BMI Weight Category
        self.data["category"] = self.data["bmi"].apply(self.get_category)
        pass

    def get_risk(self, bmi):
        # Get BMI Risk value
        self.result_list = (bmi_table_df['range_max'] >= bmi) & (bmi_table_df['range_min'] <= bmi)
        self.result_index = self.result_list[np.array(self.result_list) == True]
        self.risk = bmi_table_df["risk"][self.result_index.index[0]]
        return str(self.risk)

    def get_category(self, bmi):
        # GET BMI Category Value
        self.result_list = (bmi_table_df['range_max'] >= bmi) & (bmi_table_df['range_min'] <= bmi)
        self.result_index = self.result_list[np.array(self.result_list) == True]
        self.category = bmi_table_df["category"][self.result_index.index[0]]
        return str(self.category)

    def get_overweight_count(self):
        # GET Over Weight people Count
        total = self.data.groupby('category').count()
        total = total.transpose()["Overweight"]["Gender"]
        return total
    
    def drop_duplicates(self):
        # Drop the Duplicate Values
        self.data = self.data.drop_duplicates()

    def get_data(self):
        # Retrun Output Result Table
        return self.data
