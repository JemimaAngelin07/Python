class Company:
    def __init__(self):
        #protected member
        self._project="NLP"
class Employee(Company):
    def __init__(self,name):
        self.name=name
        Company.__init__(self)
    
    def show(self):
        print("Name:",self.name) 
        print(f"{self.name} Working on Project",self._project)

emp=Employee("Jessa")
emp.show()

# Direct access protected data member
print("Company Project:",emp._project)