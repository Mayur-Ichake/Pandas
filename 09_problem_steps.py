# I will create one excel file to show differnet problem steps

import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman","bharat"],
          "Age":[20,21,22,23,24,25,26],
          "City":["pune","Satara","nagpur","nashik","solapur","akola","amravati"],
          "salary":[100000,200000,300000,400000,500000,600000,700000] 
          }

df = pd.DataFrame(data)
print("\nSample data:\n")
print(df)

name = df["Name"]
print("\nDisplaying name column:\n")
print(name)

name_age = df[["Name","Age"]]
print("\nDisplaying name & age column:\n")
print(name_age)

# highest_salary = df[df["salary"] < 300000]
# print("\nSalary < 30000\n")
# print(highest_salary)

filtered = df[(df["Age"] < 22) & (df["salary"] < 300000)]
print("\nAge < 22 | salary < 300000\n")
print(filtered)

