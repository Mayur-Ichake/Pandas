import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman","bharat"],
          "Age":[20,21,22,23,24,25,26],
          "City":["pune","Satara","nagpur","nashik","solapur","akola","amravati"],
          "salary":[100000,200000,300000,400000,500000,600000,700000] 
          }

df = pd.DataFrame(data)
print(df)
print("\n")
df.loc[1 , "Age"] = 20
print(df)

# Suppose you have incriments salary 1%
print("\n")
df["salary"] = df["salary"] * 1.01
print(df)