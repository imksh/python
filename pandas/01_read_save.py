import pandas as pd

#? reading data

# from csv
df = pd.read_csv("pandas/data/sales_data_sample.csv",encoding="latin1")

# from excel
df = pd.read_excel("pandas/data/SampleSuperstore.xlsx")

#from json
df = pd.read_json("pandas/data/sample_Data.json")


#? Saving data 

data = {
    "Name": ["Ram","Shayam", "Karan", "Baiju","Shivam"],
    "Age": [20,28,21,30,27],
    "City":["Nagpur","Mumbai","Bhopal","Bhopal","Alamnagar"]
}
df=pd.DataFrame(data)
print(df)

#  csv
df.to_csv("pandas/data/output.csv")
df.to_csv("pandas/data/output_without_index.csv",index=False)  #No index

# excel
df.to_excel("pandas/data/output.xlsx")

# json
df.to_json("pandas/data/output.json")

