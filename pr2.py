import pandas as pd
data = pd.read_csv("student.csv")
print(data)


print(data.head())
print(data.shape)
print(data.columns)

data["Result"] = ["Pass", "Pass", "Pass"]
print(data)

print(data[["Name", "Marks"]])


print(data.isnull())

data.drop_duplicates(inplace=True)
print(data)

sorted_data = data.sort_values(by="Marks", ascending=False)
print(sorted_data)