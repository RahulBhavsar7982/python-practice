import pandas as pd

data = {
    "product":  ["Laptop", "Phone", "Tablet", "Watch", "Earbuds"],
    "price":    [50000, 30000, 20000, 5000, 2000],
    "units":    [10, 45, 20, 80, 150],
}

df=pd.DataFrame(data)

df.to_csv("sales.csv",index=False)
df2=pd.read_csv("sales.csv")
print("Sales data",df2)


df["revenue"]=df["price"]*df['units']
print("Total Revenue:",df["revenue"].sum())


best = df.loc[df["revenue"].idxmax()]
print(f" Best Seller: {best['product']} {best['revenue']}")

worst=df.loc[df["revenue"].idxmin()]
print(f"Least seller:{worst["product"]}  { worst["revenue"]}")

print(f"Product sold more than 100 units:")
print(df[df["units"] > 100])

print(f" Average Price: ₹{df['price'].mean()}")