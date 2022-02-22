import os
import argparse
import pandas as pd
from bmi_cal import BMICalculator, LoadJsonToDataFrame


# Sample BMI Input
bmi_input = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]


if __name__ == '__main__':
    cli_parser = argparse.ArgumentParser(description='BMI Calcualtor')
    cli_parser.add_argument('-i', '--json_file', type=str, default=None, help='Load json File')
    
    args = cli_parser.parse_args()
    
    if args.json_file is not None:
        if '.json' in args.json_file:
            if os.path.exists(args.json_file):
                df = LoadJsonToDataFrame(args.json_file)
                data = df.load_json()
                
                b = BMICalculator(data)
                print("Solution 1:   Calcualate BMI, BMi Category and Health Risk")
                b.drop_duplicates()
                b.calculate_bmi()
                b.calculate_category()
                print(b.get_data())
                
                print("\n Solution 2: total number of overweight people \n", b.get_overweight_count())
                
            else:
                raise FileExistsError("File Not Found")
