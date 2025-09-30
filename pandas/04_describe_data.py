import pandas as pd

df = pd.read_json("pandas/data/sample_Data.json")

# shows summary of descriptive stastics for numerical column
print(df.describe())

# knowing data

# shapes returns a tuple with two values (rows,cols)
print(df.shape)

# columns returns a names of cols
print(df.columns)


# info() :- displays info about data
df.info()