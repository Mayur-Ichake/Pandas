import pandas as pd

#  read Data frame of CSV file
df = pd.read_csv("sales_data_sample.csv" , encoding="latin 1")
print(df)

# read Data frame of excel file
"""df = pd.read_excel("SampleSuperstore.xlsx")
print(df)"""

# read Data frame of json file
# df = pd.read_json("sample_Data.json")
# print(df)