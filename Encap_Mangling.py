class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp=Employee("Jack",10000)
print("Name:",emp.name)

# direct access to private member using name mangling
print("Salary:",emp._Employee__salary)        