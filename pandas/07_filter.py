import pandas as pd

data = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "age": [20,28,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"],
    "salary": [40000,50000,35000,70000,55000]
}
df=pd.DataFrame(data)

#? Selecting columns
column = df["name"]
print(column)
subset = df[["description","price"]] #select multiple row
print(subset)

#? filtering row

filtered_row = df[df["age"]>25]
filtered_row = df[(df["age"]>25) & (df["salary"]>50000)] #multiple selection for filtering
print(filtered_row)