import pandas as pd

# df = pd.read_excel("02_output_save.xlsx")
# print(df.info())

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)
print(df.info())