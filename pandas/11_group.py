import pandas as pd
data = {
    "name": ["Ram","Shayam", "Karan", "Baiju","Shivam","Karun","Tarun","Varun"],
    "age": [20,28,20,30,20,32,24,28],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar","Nagpur","Mumbai","Delhi"],
    "salary": [40000,50000,35000,70000,55000,26000,16000,72000]
}
df=pd.DataFrame(data)

grouped=df.groupby("city")["salary"].sum() #single col


grouped=df.groupby(["city","age"])["salary"].sum() #multi col group

print(grouped)



"""
aggragate functions :-

1.sum()
2.mean()
3.count()
4.min()
5.max()
6.std()
"""