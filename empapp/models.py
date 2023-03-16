from django.db import models

# Create your models here.


class Department(models.Model):

    Name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200, default=' ')

    def __str__(self):
        return self.Name


# id:int
# name:str
# img:str
# desc:str
# price:int


class Emp(models.Model):
    # id=models.CharField(max_length=200)

    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to="pics", default='')
    dept = models.ForeignKey(
        Department,   on_delete=models.CASCADE, default='')
    salary = models.IntegerField(default=0)
    age = models.CharField(max_length=200, default='')
    hiredate = models.DateField(default='2023-02-27')
    price = models.IntegerField(default='333')
