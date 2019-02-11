class Car:
    
    def __init__(self, year, make, model, price):
        self.year = 0
        self.make = make
        self.model = model
        self.price = 0

    owner = "Kevin"


kevinCar = Car(1998,"Nissan","Altima",1000)


"""kevinCar.year=int(raw_input("What year is your car? "))
kevinCar.make = raw_input("What make is your car? ")
kevinCar.year = raw_input("What model is your car? ")
kevinCar.price=int(raw_input("How much is your car? "))"""

"""print(kevinCar.year)
print(kevinCar.make)
print(kevinCar.model)
print(kevinCar.price)
print(kevinCar.owner)"""


garage = [Car(1998,"Nissan","Altima",1000), Car(2001,"Ford","Mustang",5000), Car(1998,"Volkswagon","Edge",200)]

for x in garage:
    print(x.make)

