
import os
import pandas as pd

def read_excel(file_path, sheet_name=0):
    """Reads an Excel file and returns a DataFrame."""
    try:
        return pd.read_excel(file_path, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def write_excel(dataframe, file_path, sheet_name='Sheet1'):
    """Writes a DataFrame to an Excel file."""
    try:
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
    except Exception as e:
        print(f"Error writing Excel file: {e}")