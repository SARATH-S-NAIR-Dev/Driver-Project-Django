from django.db import models

from BasicEntry.models import District

# Create your models here.
class NewUser(models.Model):
    UserName=models.CharField(max_length=50,null=False)
    UserGender=models.CharField(max_length=10,null=False)
    UserPhone=models.CharField(max_length=13,null=False)
    UserEmail=models.EmailField(unique=True)
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    UserPassword=models.CharField(max_length=50,null=False)

class NewSeeker(models.Model):
    SeekerName=models.CharField(max_length=50,null=False)
    SeekerGender=models.CharField(max_length=10,null=False)
    SeekerDob=models.CharField(max_length=20,null=False)
    SeekerPhone=models.CharField(max_length=13,null=False)
    SeekerEmail=models.EmailField(unique=True)
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    SeekerPassword=models.CharField(max_length=50,null=False)
    PersonaldataStatus=models.CharField(max_length=5,default=0)
    TestdataStatus=models.CharField(max_length=5,default=0)
    longdrivestatus=models.CharField(max_length=5,default=0)
    
