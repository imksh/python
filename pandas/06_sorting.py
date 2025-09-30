import pandas as pd
data = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "age": [20,28,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"],
    "salary": [40000,50000,35000,70000,55000]
}
df=pd.DataFrame(data)

# df.sort_values(by=col_name, ascending=true/false,inplace)

df.sort_values(by="name",ascending= True,inplace=True) #single col

df.sort_values(by=["name","age"],ascending= [False,False],inplace=True) #multiple col

print(df)
