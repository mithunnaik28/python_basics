class movie:
    def __init__(self,tittle,rating = float):
        self.tittle = tittle
        self.rating = rating

    def display(self):
        print(f"{self.tittle} movie is getting {self.rating} ratings")

kgf = movie("kgf",8.5)
rrr = movie("RRR",6.7)

kgf.display()
rrr.display()

# kgf movie is getting 8.5 ratings
# RRR movie is getting 6.7 ratings
