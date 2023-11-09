class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    #getter method
    def get_age(self):
        return self.__age
    #setter method
    def set_age(self,age):
        self.__age=age 
stud=Student("Jesse",12)
print("Name:",stud.name,stud.get_age())

stud.set_age(15)
print("After Setting up:",stud.name,stud.get_age())