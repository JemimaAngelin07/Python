class student:
    pass
class marks:
    pass
student1=student()
marks1=marks()
print(isinstance(student1,student))
print(isinstance(marks1,student))
print(isinstance(marks1,marks))
print(isinstance(student1,marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(student,object))
print(issubclass(marks,object))