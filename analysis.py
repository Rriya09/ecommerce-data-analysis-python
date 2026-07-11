import numpy as np
import pandas as pd
df=pd.read_excel("ecom.xlsx")
df = df[["CustomerID", "Description", "Quantity", "UnitPrice"]]
df["PurchaseAmount"]=df["UnitPrice"]*df["Quantity"]
df["Description"]=df["Description"].str.strip().str.title()

print(f"Total duplicated rows:{df.duplicated().sum()}") #Check total duplicate rows
print(df[df.duplicated()])  #check obly duplicate rows    
df=df.drop_duplicates()
print(df.shape)
print(df.isnull().sum()) #check null values
df=df.dropna(subset="CustomerID")
print(df.isnull().sum())
print(df.shape)
print("\nFirst Five rows")
print(df.head())
print(df.shape)
print(df.dtypes)
print("\nSummary Statistics")
print(df.describe())


#Average purchase amount
product_avg=df.groupby("Description")["PurchaseAmount"].mean()
print(f"Average Purchase amount per product:{product_avg}")
product_std=df.groupby("Description")["PurchaseAmount"].std()
print(f"Standard Deviation of products:{product_std}")
product_total=df.groupby("Description")["PurchaseAmount"].sum()
print(f"Total sale per product:{product_total}")


top5=product_total.sort_values(ascending=False).head(5)
print(f"Top 5 items ={top5}")
lowest=product_total.sort_values().head(3)
print(f"Lowest 3 Products:{lowest}")
customers_total=df.groupby("CustomerID")["PurchaseAmount"].sum()
vip=customers_total.sort_values(ascending=False).head(10)
print(f"VIP customers:{vip}")

p25=customers_total.quantile(0.25)
p50=customers_total.quantile(0.50)
p75=customers_total.quantile(0.75)
low=customers_total[customers_total<=p25]
medium=customers_total[(customers_total>p25) & (customers_total<=p50)]
high=customers_total[ (customers_total>p50) & (customers_total<=p75)]
vip=customers_total[customers_total>p75]
print("Customer Segmentatiom:")
print("Low:", len(low))
print("Medium:", len(medium))
print("High:", len(high))
print("VIP:", len(vip))

top_trending = product_total.sort_values(ascending=False).head(5)
print("Top 5 Trending Products:")
print(top_trending)

customer=17850
bought=df[df["CustomerID"]==customer]["Description"]
all_products=df["Description"].unique()
not_bought=np.setdiff1d(all_products,bought)
recommend=product_total.loc[not_bought].sort_values(ascending=False).head(5)
print("\nRecommended Products")
print(recommend)

#Numpy time
purchase_array=df["PurchaseAmount"].to_numpy()
import time 
start=time.time()
numpy_mean=np.mean(purchase_array)
end=time.time()
print("Numpy time:",end-start)

#Python loop time
start=time.time()
total=0
for value in purchase_array:
    total+=value
count=len(purchase_array)    
loop_mean=total/count
end=time.time()
print("Loop Time:",end-start)
print("NumPy Mean:", numpy_mean)
print("Python Loop Mean:", loop_mean)
