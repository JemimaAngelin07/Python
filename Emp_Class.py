class employee():
    def __init__(self,name,age,id,salary):  
        self.name = name 
        self.age = age
        self.id = id
        self.salary=salary
 
emp1 = employee("Jack",24,12045,20000) 
emp2 = employee("John",23,12056,10000)
print(emp1.__dict__)  
print("Name:",emp2.name)
print("Age:",emp2.age)
print("Emp_ID:",emp2.id)
print("Emp_Salary:",emp2.salary)