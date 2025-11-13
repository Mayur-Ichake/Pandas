import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)
print(df)
# How to save csv file
df.to_csv("02_output_save.csv", index= False)

# How to save excel file
df.to_excel("02_output_save.xlsx" , index= False)

# How to save json file
df.to_json("02_output_save.json", index=False)