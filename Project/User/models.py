from django.db import models
from Guest.models import NewSeeker, NewUser
from BasicEntry.models import ComplaintType

# Create your models here.

class UserComplaint(models.Model):
   UserID=models.ForeignKey(NewUser,on_delete=models.CASCADE)
   ComplaintType=models.ForeignKey(ComplaintType,on_delete=models.CASCADE)
   ComplaintTitle=models.CharField(max_length=50,null=False)
   ComplaintDetails=models.CharField(max_length=200,null=False)
   Reply=models.CharField(max_length=200,null=True)
   Status=models.BooleanField(default=False)
   ComplaintDate=models.DateTimeField(auto_now=True)