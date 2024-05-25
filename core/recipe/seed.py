from faker import Faker
from .models import *
import random
from django.db.models import Sum

fake=Faker()

def create_subjects_marks(n):

    try:
        student_obj= student.objects.all()
        for students in student_obj:
            subjects= subject.objects.all()
            for sub in subjects:
                sunjectmarks.objects.create(
                    
                    student= students,
                    subject= sub,
                    marks= random.randint(0,100),

                )
    except Exception as e:
        print(e)

def total_marks():
    students_with_total= student.objects.annotate(total_marks_sum = Sum('studentmarks__marks'))
    for std in students_with_total:
        student_subject_marks= sunjectmarks.objects.filter(student=std)
        total_marks_sum = std.total_marks_sum if std.total_marks_sum else 0
        student_subject_marks.update(show_total_marks= total_marks_sum)
        
        


total_marks()

def seed_db(n=10)-> None:
    try:
        for _ in range (n):
            
            dept_obj= Department.objects.all()
            random_dept= random.randint(0, len(dept_obj)-1)
            
            department= dept_obj[random_dept]
            student_id= f'BC{random.randint(100,999)}'
            student_name= fake.name()
            email= fake.email()
            student_age= random.randint(20,30)
            student_address= fake.address()


            student_id_obj= studentID.objects.create(student_ID= student_id)

            student_obj=student.objects.create(
                department= department,
                student_id= student_id_obj,
                student_name= student_name,
                email= email,
                student_age= student_age,
                student_address= student_address

            )
    except Exception as e:
        print(e)