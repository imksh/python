import pandas as pd

df = pd.read_json("pandas/data/sample_Data.json")

#? head() and tail() default show 5 rows

# top 10 rowss
print(df.head(10))

#bottom 10 rows
print(df.tail(10))
