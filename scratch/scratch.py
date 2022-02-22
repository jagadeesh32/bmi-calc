import pandas as pd

bmi_input = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

bmi_table = [
    {"category": "Underweight", "range_min": 0, "range_max": 18.4, "risk": "Malnutrition risk"},
    {"category": "Normal weight", "range_min": 18.5, "range_max": 24.9, "risk": "Low risk"},
    {"category": "Overweight", "range_min": 25, "range_max": 29.9, "risk": "Enhanced risk"},
    {"category": "Moderately obese", "range_min": 30, "range_max": 34.9, "risk": "Medium risk"},
    {"category": "Severely obese", "range_min": 35, "range_max": 39.9, "risk": "High risk"},
    {"category": "Very severely obese", "range_min": 40, "range_max": 0, "risk": "Very high risk"},
]


bmi_table_df = pd.DataFrame(bmi_table)
bmi_table_df.head()

bmi_df = pd.DataFrame(bmi_input)
bmi_df.head()

bmi_df["bmi"] = round(bmi_df['WeightKg'] / (bmi_df['HeightCm']/100) ** 2, 2)
bmi_df.head()

def get_risk(bmi):
    result_list = list(bmi_table_df['range_max'] >= bmi) & (bmi_table_df['range_min'] <= bmi)
    result_index = result_list[result_list == True]
    risk = bmi_table_df["risk"][result_index.index[0]]
    return str(risk)

def get_category(bmi):
    result_list = list(bmi_table_df['range_max'] >= bmi) & (bmi_table_df['range_min'] <= bmi)
    result_index = result_list[result_list == True]
    risk = bmi_table_df["category"][result_index.index[0]]
    return str(risk)

bmi_df["risk"] = bmi_df["bmi"].apply(get_risk)
bmi_df["category"] = bmi_df["bmi"].apply(get_category)


print(bmi_df.head())
