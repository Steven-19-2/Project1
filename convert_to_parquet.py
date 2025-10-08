import pandas as pd
from dataclasses import dataclass
   
@dataclass
class covert_to_parquet:
    def convert(self):
        df = pd.read_csv('employees_data1.csv')
        df.to_parquet('employee_data1.parquet', index=False)
        print("CSV file has been converted to Parquet format and saved as 'employee_data1.parquet'")


if __name__ == "__main__":
    converter = covert_to_parquet()
    converter.convert()
    
