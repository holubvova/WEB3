from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField("name", max_length= 200)
    user_surname = models.CharField("surname",max_length=200)
    user_email = models.EmailField("email", max_length=45)
    user_password = models.CharField("password", max_length=25)
    user_tell = models.IntegerField("tell")
    user_birthday = models.DateField("birthday")
    user_booking = models.DateField("booking")
    user_gender = models.CharField("sex",max_length=25)

    def __str__(self):
       return f'{self.user_name, self.user_surname,self.user_email,self.user_birthday.__str__(),self.user_gender,self.user_booking.__str__(),self.user_tell}'