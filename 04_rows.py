"""
head() = by default first 5 rows show in display
tail() = by default last 5 rows show in display
"""
import pandas as pd
df = pd.read_json("sample_Data.json")
print("\nDisplay first 5 rows")
print(df.head())

print("\nDisplay last 5 rows")
print(df.tail())