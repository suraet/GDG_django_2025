class Employee :
    def __init__(self,name ,salary:int):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary*12
a = Employee('surafel',120000)

print( a.name ,"u have yearly salary " ,a.annual_salary())