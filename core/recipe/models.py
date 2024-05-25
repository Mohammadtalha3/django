from django.db import models
from django.contrib.auth.models import  User, AbstractUser
from django.contrib.auth import get_user_model

User= get_user_model()

# Create your models here.


class Recipes(models.Model):
    user=  models.ForeignKey(User, on_delete=models.SET_NULL, null=True , blank=True)
    recipe_name= models.TextField(max_length=100)
    description= models.TextField()
    image= models.ImageField(upload_to="images")
    recipe_view_count= models.IntegerField(default=1)


class Department(models.Model):
    department= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering= ['department']


class studentID(models.Model):
    student_ID= models.CharField(max_length=50)

    def __str__(self) -> str:
        return  self.student_ID

class subject(models.Model):
    subject_name= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    
  
class student(models.Model):
    department= models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id= models.OneToOneField(studentID,related_name='Id', on_delete=models.CASCADE)
    student_name= models.CharField(max_length=70)
    email= models.EmailField(unique=True)
    student_age= models.IntegerField(default=18)
    student_address= models.TextField()
    Total_marks= models.IntegerField(default=0)

    def  __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering= ['student_name']
        verbose_name= "student"


class sunjectmarks(models.Model):
    
    student= models.ForeignKey(student, related_name='studentmarks', on_delete=models.CASCADE)
    subject= models.ForeignKey(subject, on_delete= models.CASCADE)
    marks= models.IntegerField()
    show_total_marks= models.IntegerField( default= 0)
    


    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
        unique_together= ['student', 'subject']


    

    
