class Employee:
    def __init__(self,name,salary):
        self.name=name
        #private member
        self.__salary=salary
    def show(self):
        print("Name:",self.name,"\nSalary:",self.__salary)

emp=Employee("Jabez",25000)
emp.show()            