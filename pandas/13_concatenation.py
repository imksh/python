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


#? pf.concat([df1,df2],axis=0,ignore_index=true)
# axis = 1 for horizontal[row wise], 0 for vertical[column wise]
# ignore index - reset to new index

#? concat vertically
conVer = pd.concat([df1,df2],axis=0,ignore_index=True)
print("Vertically: ")
print(conVer)

#? concat Horizontally
conHor = pd.concat([df1,df2],axis=1,ignore_index=True)
print("Horizontally: ")
print(conHor)