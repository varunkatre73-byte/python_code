import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Dataset.csv")

data.head()

data.info()

data.columns = data.columns.str.strip()
print(data.columns)

plt.figure(figsize=(8, 5))
plt.hist(data["age"], bins=20)
plt.xlabel("age")
plt.ylabel("Frequency")
plt.title("Histogram of age")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["annual Salary"], bins=20)
plt.xlabel("annual Salary")
plt.ylabel("Frequency")
plt.title("Histogram of annual Salary")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["credit card debt"], bins=20)
plt.xlabel("credit card debt")
plt.ylabel("Frequency")
plt.title("Histogram of credit card debt")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["net worth"], bins=20)
plt.xlabel("net worth in lakh")
plt.ylabel("Frequency")
plt.title("Histogram of net worth")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["car purchase amount"], bins=20)
plt.xlabel("car purchase amount")
plt.ylabel("Frequency")
plt.title("Histogram of car purchase amount")
plt.show()