import pandas as pd

# df = pd.read_json("sample_Data.json")
# print("\nDisplaying info data\n")
# print(df.info())


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)
print("\nDisplaying info data\n")
print(df.info())