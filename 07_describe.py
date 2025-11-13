import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman","bharat"],
          "Age":[21,20,22,29,24,30,26],
          "City":["pune","satara","Ayodha","nashik","solapur","akola","amravati"],
          "salary":[10000,20000,30000,40000,50000,60000,70000] 
          }

df = pd.DataFrame(data)
print("\n sample data:\n")
print(df)
print("\nDescribe data:\n")
print(df.describe())