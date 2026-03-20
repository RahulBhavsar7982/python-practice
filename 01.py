
students = [
    {"name": "Ali", "grades": [85, 90, 78]},
    {"name": "Sara", "grades": [92, 88, 95]},
    {"name": "John", "grades": [60, 55, 70]},
    {"name": "Mia", "grades": [75, 80, 85]},
]


def average(grade):
    return sum(grade) / len(grade)

result=[]
for student in students:
    name =student['name']
    grades=student['grades'] 
    avg=average(grades)
    result.append({"name":name,"avg":avg})
    print(f" {name}, Avergae:{round(avg,2)}")

highest=max(result,key= lambda x:x['avg'])
lowest=min(result,key=lambda x:x['avg'])

print(f"\nHighest:{highest['name']},({round(highest['avg'],2)})")
print(f"Lowest:{lowest['name']},({round(lowest['avg'],2)})")