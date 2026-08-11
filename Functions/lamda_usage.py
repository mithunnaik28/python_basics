students=[
    {"name":"mithun","marks":83},
    {"name":"tejas","marks":97},
    {"name":"bhoomika","marks":79}
]
students.sort(key= lambda x: x["marks"],reverse=True)

print(students)

# [{'name': 'tejas', 'marks': 97}, {'name': 'mithun', 'marks': 83}, {'name': 'bhoomika', 'marks': 79}]
