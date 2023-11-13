from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    image = models.ImageField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username
    

class Student(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    nid = models.IntegerField()
    phone = models.IntegerField()
    dept = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.account.username
    
    def username(self):
        return self.account.username


class Room(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room_number = models.IntegerField()



class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.room.student.account.username

    def username(self):
        return self.student.account.username
    
    def room_num(self):
        return self.room.room_number