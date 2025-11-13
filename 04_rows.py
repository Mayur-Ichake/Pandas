"""
head() = by default first 5 rows show in display
tail() = by default last 5 rows show in display
"""
import pandas as pd

df = pd.read_excel("SampleSuperstore.xlsx")
#  First 5 rows
print("Showing first 5 rows \n")
op = df.head(5)
print(op)

# Last 5 rows
print("showing last 5 rows \n")
km = df.tail(5)
print(km)

op.to_excel("04_First_5_rows.xlsx" , index=False)
km.to_excel("04_Last_5_rows.xlsx" , index=False)