import pandas as pd

data = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "age": [20,28,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"],
    "salary": [40000,50000,35000,70000,55000]
}
df=pd.DataFrame(data)

#? adding

# assignment method
df["score"]=[70,80,90,67,43]
df["bonus"]=df["salary"]*0.1


# using insert method 
# df.insert(loc(indx),"col_name",data)
df.insert(0,"id",[1,2,3,4,5])

print(df)