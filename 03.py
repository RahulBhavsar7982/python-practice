import json 

data=[]

def add_student():
    s=input("Enter student name:")
    g1=int(input("Enter student marks:"))
    g2=int(input("Enter student marks:"))
    g3=int(input("Enter student marks:"))
    avg=round((g1+g2+g3) / 3,2)
    data.append({"name":s,"avg":avg})
    print(f" {s} saved")

while True:
    add_student()
    choice=input("add student (yes/no):")
    if choice=="no":
        break

with open("data,json","w" ) as f:
    json.dump(data,f)

print("\n Final Result")
for student in data:
    print(f"{student['name'] ,{student['avg']}}")


highest=max(data,key= lambda x:x['avg'])
lowest=min(data,key=lambda x:x['avg'])

print(f"\nHighest:{highest['name']},({round(highest['avg'],2)})")
print(f"Lowest:{lowest['name']},({round(lowest['avg'],2)})")