from datetime import date
class Person:
    def __init__(self,name,country,DOB):
        self.name=name
        self.country=country
        self.DOB=DOB
    def cal_age(self):
        today=date.today()
        age=today.year - self.DOB.year
        if today < date(today.year,self.DOB.month,self.DOB.day):
            age -=1
        return age
person1=Person("John","USA",date(1989,7,24))
person2=Person("Jemi","India",date(1994,3,19))
person3=Person("Jabez","Canda",date(1995,8,12))

print("NAME:",person1.name)
print("COUNTRY:",person1.country)
print("DateOfBirth:",person1.DOB)
print("AGE:",person1.cal_age())

print("NAME:",person2.name)
print("COUNTRY:",person2.country)
print("DateOfBirth:",person2.DOB)
print("AGE:",person2.cal_age())

print("NAME:",person3.name)
print("COUNTRY:",person3.country)
print("DateOfBirth:",person3.DOB)
print("AGE:",person3.cal_age())
