class Employee:
    def __init__(self,name, designation ="worker",salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display(self):
        print(f"Name:{self.name}\ndesignation:{self.designation}\nsalary:{self.salary}\n")

mithun = Employee("Mithun","ai eng",500000)
rama = Employee("Rama")

mithun.display()
rama.display()
        
# Name:Mithun
# designation:ai eng
# salary:500000

# Name:Rama
# designation:worker
# salary:30000        
