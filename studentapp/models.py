from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 0)
    borrowed = models.BooleanField(default= False)
    class Meta:
        db_table = "Book"
    
    def __str__(self):
        return self.title
class Student(models.Model):
    name = models.CharField(max_length = 100 )
    email = models.EmailField()

    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.name
class Borrowing(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name = "borrowing_student")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name= "borrowing_book")
    returned = models.BooleanField(default=False)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(auto_now_add=True)
    renewed = models.BooleanField(default=False)

    class Meta:
        db_table = 'Borrowing'
    def ___str__(self):
        return self.student
