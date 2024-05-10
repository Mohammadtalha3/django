from faker import Faker
from .models import *
import random

fake=Faker()

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