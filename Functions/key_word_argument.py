def student_info(**details): # ** is dictionary 
    for key, value in details.items():
        print(f"{key}:{value}")

student_info(name="mithun",age=18,rollnumber=32)

# name:mithun
# age:18
# rollnumber:32
