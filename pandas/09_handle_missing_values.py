import pandas as pd

data = {
    "name": ["Ram",None, "Karan", "Baiju","Shivam"],
    "age": [20,40,21,30,27],
    "city":["Nagpur","Mumbai","Bhopal","Bhopal",None],
    "salary": [None,50000,35000,None,55000],
    "value":[10,20,None,40,50],
}
df=pd.DataFrame(data)

#? detecting null values

# nan - not a number for numbers
# none - for objects
# isnull() - returns true for null values and false for values present


print(df.isnull()) # returns true and false for each value

print(df.isnull().sum()) # returns sum of null valuse for each column

#? removing null values

# removes rows
df.dropna(inplace=True)

# removes rows
df.dropna(axis=0,inplace=True)

# removes column
df.dropna(axis=1,inplace=True)


#? filling null valuse
# fillna(val,inplace=True)
df.fillna(0,inplace=True) #default value to all na

# calculated value
df["salary"].fillna(df["salary"].mean(),inplace=True)


#? Interpolation
# fillsna by estimated value
# df.interpolate(method,axis,inplace) -> axis=0 - rows, axis=1 - column
# interpolate has many methods mainly having linear,polynomial,time

df["value"] = df["value"].interpolate(method="linear")

df.interpolate(method="linear",axis=0,inplace=True)

print(df)