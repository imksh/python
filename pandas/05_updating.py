import pandas as pd

data = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "age": [20,28,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"],
    "salary": [40000,50000,35000,70000,55000]
}
df=pd.DataFrame(data)

#? loc -location
# loc[row_index,"col_name"]= new_val
df.loc[2,"age"]=80

#? updating col
df["salary"]=df["salary"]*1.05
print(df)
