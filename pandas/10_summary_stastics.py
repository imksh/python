import pandas as pd
data = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "age": [20,28,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"],
    "salary": [40000,50000,35000,70000,55000]
}
df=pd.DataFrame(data)

print(df)

print(df["age"].mean())
print(df["age"].sum())
print(df["age"].min())
print(df["age"].max())

