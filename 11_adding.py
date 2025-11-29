import pandas as pd

data = {  "Name":["mayur","shreya","ram","sita","gita","laxman","bharat"],
          "Age":[20,21,22,23,24,25,26],
          "City":["pune","Satara","nagpur","nashik","solapur","akola","amravati"],
          "salary":[100000,200000,300000,400000,500000,600000,700000] 
          }

df = pd.DataFrame(data)
print(df)

print("\nAdding new column \'State\':\n")
df["State"]= ("Maharastra")
print(df)

# now i want to insert position & data

print("\nReplace city to salary & salary to city\n")
df.insert(0, "Employee Id",['Ma29','Sa16','sdf34','dg34','fh34','fh22','df42'])
print(df)