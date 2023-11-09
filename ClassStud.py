class Student:
    school='Monfort CBSE'
    address='Sriperbumdur,Kanchipuram'
student1=Student()
student2=Student()
student1.student_id="S123"
student1.student_name="Jovina"
student2.student_id="S123"
student2.marks_langusge= 90
student2.marks_science= 95
student2.marks_maths= 98
students=[student1,student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr}->{getattr(student,attr)}')