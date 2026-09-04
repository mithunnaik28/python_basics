class Mobile:
    def __init__(self,brand,price):
        self.brand = brand 
        self.price = price 

    def show_mobiles(self):
        return (f"{self.brand} mobile price is {self.price}")

redmi = Mobile("redmi 14c",11000)
iphone = Mobile("iphone 18pro max",139000)

redmi.show_mobiles()
iphone.show_mobiles()
