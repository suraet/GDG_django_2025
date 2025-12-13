class Vehicle :
    def __init__(self, brand , year):
        self.brand= brand
        self.year = year 
    def info(self):
        print(self.brand , self.year)

class Car(Vehicle):
    def __init__(self,brand, model ):
        self.model= model
        self.brand=brand
    def info(self):
        print(self.brand, "",self.model)

a= Vehicle("toyota",2150)
car_model = Car("honda","civic")

car_model.info()
a.info()