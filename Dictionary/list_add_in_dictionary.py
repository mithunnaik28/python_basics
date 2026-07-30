student=["mithun","annappa","naik"]
marks=[99,65,85]

#one way
student_marks={}
for index,students in enumerate(student):
    student_marks[students]=marks[index]

print(student_marks)

#another way
student_marks1={}
for i in range(len(student)):
    student_marks1[student[i]]=marks[i]

print(student_marks1)

# {'mithun': 99, 'annappa': 65, 'naik': 85}
# {'mithun': 99, 'annappa': 65, 'naik': 85}
