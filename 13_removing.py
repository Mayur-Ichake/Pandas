import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman","bharat"],
          "Age":[20,21,22,23,24,25,26],
          "City":["pune","Satara","nagpur","nashik","solapur","akola","amravati"],
          "salary":[100000,200000,300000,400000,500000,600000,700000],
          "experience":[1,2,3,4,4,5,5]
          }

df = pd.DataFrame(data)
print(df)

# i want to remove experience column
df.drop(columns= ["experience","salary"],inplace=True)
print("\nRemoving the experience and salary column\n")
print(df)