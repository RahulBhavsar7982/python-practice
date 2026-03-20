import json


students = [
    {"name": "Ali", "grades": [85, 90, 78]},
    {"name": "Sara", "grades": [92, 88, 95]},
    {"name": "John", "grades": [60, 55, 70]},
    {"name": "Mia", "grades": [75, 80, 85]},
]

def average(grades):
    return sum(grades) / len(grades)

data=[]
for student in students:
    name=student['name']
    grades=student['grades']
    avg=round(average(grades),2)
    data.append({"name":name,"avg":avg})
  

with open("results.json", "w") as f:
    json.dump(data, f)

with open("results.json", "r") as f:
    data = json.load(f)

print("Results saved to results.json")

print("\n Loaded from file:")
for student in data:
    print(f"{student['name']} → {student['avg']}")