class Student:
    def __init__(self,name:str,marks:int):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"{self.name} is given mark {self.marks}")

mithun = Student("mithun",83)
tejas = Student("tejas",97)

mithun.display_info()
tejas.display_info()
