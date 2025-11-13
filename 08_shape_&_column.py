import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman","bharat"],
          "Age":[20,21,22,23,24,25,26],
          "City":["pune","mumbai","nagpur","nashik","solapur","akola","amravati"],
          "salary":[10000,20000,30000,40000,50000,60000,70000] 
          }

df = pd.DataFrame(data)
print(df)
print(f"shape of dataSet: {df.shape}\n")
print(f"Column Names: {df.columns}\n")