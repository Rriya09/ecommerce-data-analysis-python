import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("ecom.xlsx")
df = df[["CustomerID", "Description", "Quantity", "UnitPrice"]]
df["PurchaseAmount"]=df["UnitPrice"]*df["Quantity"]
df["Description"]=df["Description"].str.strip().str.title()

print(f"Total duplicated rows:{df.duplicated().sum()}") #Check total duplicate rows
print(df[df.duplicated()])  #check only duplicate rows    
df=df.drop_duplicates()
print(df.shape)
print(df.isnull().sum()) #check null values
df=df.dropna(subset="CustomerID") #Drop row with null customersid
print(df.isnull().sum())
print(df.shape)
print("\nFirst Five rows")
print(df.head())
print(df.shape)
print(df.dtypes)
print("\nSummary Statistics")
print(df.describe())


#Average and standard daviation of purchase amount
product_avg=df.groupby("Description")["PurchaseAmount"].mean()
print(f"Average Purchase amount per product:{product_avg}")
product_std=df.groupby("Description")["PurchaseAmount"].std()
print(f"Standard Deviation of products:{product_std}")

#Total Sale per product
product_total=df.groupby("Description")["PurchaseAmount"].sum()
print(f"Total sale per product:{product_total}")

#Top 5 Products
top5=product_total.sort_values(ascending=False).head(5)
print(f"Top 5 items ={top5}")
#Lowest 3 products
lowest=product_total.sort_values().head(3)
print(f"Lowest 3 Products:{lowest}")

customers_total=df.groupby("CustomerID")["PurchaseAmount"].sum()

#VIP Customers 
Vip=customers_total.sort_values(ascending=False).head(10)
print("VIP customers:",Vip)

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

df.to_csv("analized.csv",index="False")

#Top 10 products bar chat
top10=product_total.sort_values(ascending=False).head(10)
top10.plot(kind="bar",label="Total Sales",color="blue")
plt.xlabel('Products',size=15)
plt.ylabel('Total Sales',size=15)
plt.title("Top 10 Products ",size=20)
plt.legend()
plt.tight_layout()

plt.savefig("top10.png",dpi=300,bbox_inches="tight")
plt.show()

#Top 10 VIP cutomers
vip.head(10).plot(kind="bar",label="VIP Customers",color="green")
plt.title("Top 10 VIP Customers by Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Spending")
plt.legend()
plt.tight_layout()

plt.savefig("top10VIP.png",dpi=300,bbox_inches="tight")
plt.show()

#Customer Spending Distribution
plt.hist(customers_total,bins=30,color="purple",edgecolor="black")
plt.title("Customer Spending Distribution")
plt.xlabel("Total Spending ")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customer_spending_distribution.png",dpi=300,bbox_inches="tight")
plt.show()

#Customer Segment
values=[len(low),len(medium),len(high),len(vip)]
plt.pie(values,labels=['Low','Medium','High','VIP'],colors=['r','g','lightblue','y'],autopct='%1.1f%%')
plt.title("Customer Segmentation")

plt.tight_layout()

plt.savefig("Customer_segment.png",dpi=300,bbox_inches="tight")
plt.show()

#Sctter plot
plt.figure(figsize=(8,5))
plt.scatter(df["Quantity"],df["PurchaseAmount"],color="red",marker='o',alpha=0.3)
plt.xlabel("Quantity")
plt.ylabel("Purchase Amount")
plt.grid(True)
plt.title("Quantity VS Purchase Amount")
plt.savefig("Scatter_plot.png",dpi=300,bbox_inches="tight")
plt.show()

print(df["Quantity"].sort_values(ascending=False))