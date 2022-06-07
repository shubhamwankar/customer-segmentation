import pandas as pd

# Reading the data
data1 = pd.read_excel('customer-segmentation\online_retail_II.xlsx', sheet_name=0)
data2 = pd.read_excel('customer-segmentation\online_retail_II.xlsx', sheet_name=1)

data = pd.concat([data1, data2], ignore_index=True)

print(f"data 1 rows = {data1.shape[0]}")
print(f"data 2 rows = {data2.shape[0]}")
print(f"data rows = {data.shape[0]}")

print(data.tail())