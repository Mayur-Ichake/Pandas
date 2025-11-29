import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman",None],
          "Age":[20,21,22,23,None,25,26],
          "City":["pune","Satara","nagpur","nashik","solapur","akola",None],
          "salary":[100000,200000,300000,400000,500000,600000,None],
          "experience":[1,2,3,4,4,5,None]
          }

df = pd.DataFrame(data)
print(df)

# midssing data remove dropna method
print("\n")
df.dropna(inplace=True,ignore_index=True)
print(df)