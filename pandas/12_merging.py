import pandas as pd
data1 = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "age": [20,28,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"],
}

data2 = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Kishan"],
    "salary": [40000,50000,35000,70000,55000]
}
df1=pd.DataFrame(data1)

df2=pd.DataFrame(data2)



# pd.merge(df1,df2,on="col_name",how="type of join")
#type of join - inner,outer,left,right

merged_inner = pd.merge(df1,df2,on="name",how="inner")
print("Inner")
print(merged_inner)


merged_outer = pd.merge(df1,df2,on="name",how="outer")
print("Outter")
print(merged_outer)


merged_left = pd.merge(df1,df2,on="name",how="left")
print("Left")
print(merged_left)


merged_right = pd.merge(df1,df2,on="name",how="right")
print("Right")
print(merged_right)

merged_cross = pd.merge(df1,df2,how="cross")
print("Cross")
print(merged_cross)