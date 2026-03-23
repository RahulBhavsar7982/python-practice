import matplotlib.pyplot as plt
import pandas as pd 

data = {
    "employee": ["Rahul", "Sneha", "Ali", "Raj", "Priya"],
    "jan":      [45000, 62000, 38000, 71000, 55000],
    "feb":      [52000, 58000, 41000, 68000, 60000],
    "mar":      [48000, 70000, 35000, 65000, 72000],
}

df=pd.DataFrame(data)
df.to_csv("sales_report.csv",index=False)
df2=pd.read_csv("sales_report.csv")
print("\nEmployee Data")
print(df2)


df["total"]=df["jan"]+df["feb"]+df["mar"]

best=df.loc[df["total"].idxmax()]
worst=df.loc[df["total"].idxmin()]
print(f"\nBest Performer: {best["employee"]} {best["total"]}")


print("\nAverage Sales")
avg=df["total"].mean()
print(avg)
print("\n Employee above average")
print(df[df["total"] > avg] [["employee","total"]])

print("\n Total Sales per employee")
print(df[["employee","total"]])


#Bar Chart
colours="blue","green","yellow","red","orange"
plt.bar(df["employee"],df["total"],color=colours)
plt.title("Total sales per Employee")
plt.xlabel("employee")
plt.ylabel("total")
for i,value in enumerate(df["total"]):
    plt.text(i,value + 1000,f"{value}",ha="center")
plt.show()

#Pie Chart
plt.pie(df["total"],labels=df["employee"],autopct= "%1.1f%%")
plt.title("Sales Distribustion")
plt.show()

#Line Chart
months=["jan","feb","march"]
for _,row in df.iterrows():
    plt.plot(months,[row["jan"],row["feb"],row["mar"]],marker="o",label=row["employee"])

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()