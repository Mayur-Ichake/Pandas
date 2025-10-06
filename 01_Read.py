import pandas as pd
# for csv file 
# dataframe = pd.read_csv("sales_data_sample.csv" , encoding="latin1")
# print(dataframe)

# for excel file
# df = pd.read_excel("SampleSuperstore.xlsx")
# print(df)

# for json file
df = pd.read_json("sample_Data.json")
# df = pd.read_excel("output_save.xlsx")
print(df)