from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from BasicEntry.models import ComplaintType, DriveHour, DriveMode, SeekerTestQuestion,ShortTravelingPurpose,District,LongTravelingPurpose,PackageTravelingPurpose, VehicleModel, VehicleType, Weekday
from Guest.models import NewSeeker, NewUser

# Create your models here.

class SeekerRegistration(models.Model):
   SeekerLicenseNumber=models.CharField(max_length=50,null=False,unique=True)
   SeekerLicenseProof=models.FileField(upload_to="Seeker/LicenseProof/",null=True)
   SeekerAadharNumber=models.CharField(max_length=50,null=False,unique=True)
   SeekerAadharProof=models.FileField(upload_to="Seeker/AadharProof/",null=True)
   SeekerEyeTest=models.FileField(upload_to="Seeker/EyeTestProof/",null=False)
   SeekerAdress=models.EmailField(max_length=50,null=False)
   SeekerDisability=models.CharField(max_length=50,null=False)
   SeekerDisabilityProof=models.FileField(upload_to="Seeker/DisabilityProof/",null=True)
   SeekerBadge=models.CharField(max_length=50,null=False)
   SeekerBadgeProof=models.FileField(upload_to="Seeker/BadgeProof/",null=True)
   SeekerOffence=models.CharField(max_length=50,null=False)
   SeekerRestriction=models.EmailField(max_length=50,null=False)
   SeekerID=models.ForeignKey(NewSeeker,on_delete=models.CASCADE,null=True)

class SeekerTest(models.Model):
   SeekerID=models.ForeignKey(NewSeeker,on_delete=models.CASCADE)
   TestQuestion=models.ForeignKey(SeekerTestQuestion,on_delete=models.CASCADE)
   TestAnswer=models.CharField(max_length=10,null=False)
  
   

# ===========Short Drive Management==========================

class SeekerProfileShortDrive(models.Model):
   SeekerID=models.ForeignKey(NewSeeker,on_delete=models.CASCADE)
   ShortDriveDrivingMode=models.ForeignKey(DriveMode,on_delete=models.CASCADE)
   ShortDriveDrivingHours=models.ForeignKey(DriveHour,on_delete=models.CASCADE)
   ShortDriveEligibility=models.CharField(max_length=5,null=True)
   ShortDriveAmount=models.CharField(max_length=10,null=False)

class ShortDriveWorkingdays(models.Model):
   SeekerShortDrive=models.ForeignKey(SeekerProfileShortDrive,on_delete=models.CASCADE)
   WorkingDays=models.ForeignKey(Weekday,on_delete=models.CASCADE)


class ShortDriveVehicleModels(models.Model):
   SeekerShortDrive=models.ForeignKey(SeekerProfileShortDrive,on_delete=models.CASCADE)
   VehicleModel=models.ForeignKey(VehicleModel,on_delete=models.CASCADE)

class ShortDrivePurposes(models.Model):
   SeekerShortDrive=models.ForeignKey(SeekerProfileShortDrive,on_delete=models.CASCADE)
   Purposes=models.ForeignKey(ShortTravelingPurpose,on_delete=models.CASCADE)


class ShortDriverBooking(models.Model):
   SeekerShortDriveid=models.ForeignKey(SeekerProfileShortDrive,on_delete=models.CASCADE,null=True)
   UserID=models.ForeignKey(NewUser,on_delete=models.CASCADE)
   ShortDriveBookingDate=models.DateField(auto_now_add=True)
   ShortDriveBookingTime=models.TimeField(auto_now_add=True)

   ShortDriveBookingPickingDate=models.CharField(max_length=20,null=True)
   ShortDriveBookingPickingTime=models.CharField(max_length=20,null=True)
   ShortDriveBookingPickingLocation=models.CharField(max_length=20,null=True)

   ShortDriveBookingDropingTime=models.CharField(max_length=20,null=True)
   ShortDriveBookingDropLocation=models.CharField(max_length=20,null=True)
   
   ShortDriveBookingIsReturn=models.CharField(max_length=20,null=True)
   ShortDrivePurpose=models.CharField(max_length=20,null=True)
   ShortDriveVehicleModel=models.CharField(max_length=20,null=True)
   ShortDriveBookingAmount=models.CharField(max_length=20)
   Status=models.IntegerField(default=0)
   moreinfo=models.TextField(default="No Data")
   actualtotalamount=models.CharField(max_length=20,default="00.00")
   workcompletionremarks=models.CharField(max_length=20,default="No Remarks")




# ==================End Short Drive Management========================================





# =====================Long Drive Management======================================

class SeekerProfileLongDrive(models.Model):
   SeekerID=models.ForeignKey(NewSeeker,on_delete=models.CASCADE)
   LongDriveDrivingMode=models.ForeignKey(DriveMode,on_delete=models.CASCADE)
   LongDriveDrivingHours=models.ForeignKey(DriveHour,on_delete=models.CASCADE)
   LongDriveEligibility=models.CharField(max_length=5,null=True)
   LongDriveAmount=models.CharField(max_length=10,null=False)


class LongDriveWorkingdays(models.Model):
   SeekerLongDrive=models.ForeignKey(SeekerProfileLongDrive,on_delete=models.CASCADE)
   WorkingDays=models.ForeignKey(Weekday,on_delete=models.CASCADE)

class LongDriveVehicleModels(models.Model):
   SeekerLongDrive=models.ForeignKey(SeekerProfileLongDrive,on_delete=models.CASCADE)
   VehicleModel=models.ForeignKey(VehicleModel,on_delete=models.CASCADE)

class LongDrivePurposes(models.Model):
   SeekerLongDrive=models.ForeignKey(SeekerProfileLongDrive,on_delete=models.CASCADE)
   Purposes=models.ForeignKey(LongTravelingPurpose,on_delete=models.CASCADE)

class LongDriverBooking(models.Model):
   SeekerLongdrive=models.ForeignKey(SeekerProfileLongDrive,on_delete=models.CASCADE)
   UserID=models.ForeignKey(NewUser,on_delete=models.CASCADE)
   LongDriveDistrictID=models.ForeignKey(District,on_delete=models.CASCADE)
   LongDriveLocation=models.CharField(max_length=30,null=False)
   LongDriveStartDate=models.DateField(max_length=20)
   LongDriveStartTime=models.TimeField(null=True)
   LongDriveEndDate=models.DateField(max_length=20)
   LongDriveEndTime=models.TimeField(null=True)
   LongDrivePurpose=models.CharField(max_length=20,null=True)
   LongDriveVehicleModel=models.CharField(max_length=20,null=True)
   LongDriveBookingAmount=models.CharField(max_length=20)
   moreinfo=models.TextField(default="No Data")
   actualtotalamount=models.CharField(max_length=20,default="00.00")
   workcompletionremarks=models.CharField(max_length=20,default="No Remarks")
   Status=models.IntegerField(default=0)
class LongTripDays(models.Model):
   LongDriveID=models.ForeignKey(LongDriverBooking,on_delete=CASCADE)
   LongDriveDay=models.CharField(max_length=5,null=False)
   LongDriveLocation=models.CharField(max_length=30,null=False)
   LongDriveStatus=models.CharField(max_length=10,null=False)




# ========================End Long Drive Management=====================================





# =================================Package Management====================================


class SeekerProfilePackage(models.Model):
   SeekerID=models.ForeignKey(NewSeeker,on_delete=models.CASCADE)
   PackageDrivingMode=models.ForeignKey(DriveMode,on_delete=models.CASCADE)
   PackageDrivingHours=models.ForeignKey(DriveHour,on_delete=models.CASCADE)
   PackageEligibility=models.CharField(max_length=5,null=True)
   PackageAmount=models.CharField(max_length=10,null=False)

   def __str__(self):
       return self.SeekerID.SeekerName
   

class PackageWorkingdays(models.Model):
   SeekerPackage=models.ForeignKey(SeekerProfilePackage,on_delete=models.CASCADE)
   WorkingDays=models.ForeignKey(Weekday,on_delete=models.CASCADE)

class PackageVehicleModels(models.Model):
   SeekerPackage=models.ForeignKey(SeekerProfilePackage,on_delete=models.CASCADE)
   VehicleModel=models.ForeignKey(VehicleModel,on_delete=models.CASCADE)

class PackagePurposes(models.Model):
   SeekerPackage=models.ForeignKey(SeekerProfilePackage,on_delete=models.CASCADE)
   Purposes=models.ForeignKey(PackageTravelingPurpose,on_delete=models.CASCADE)


class PackageBooking(models.Model):
   SeekerPackage=models.ForeignKey(SeekerProfilePackage,on_delete=models.SET_NULL,null=True)
   UserID=models.ForeignKey(NewUser,on_delete=models.CASCADE)
   Fromdate=models.DateField()
   Todate=models.DateField()
   TotalAmount=models.FloatField()
   Picktime=models.CharField(max_length=10,null=True)
   Droptime=models.CharField(max_length=10,null=True)
   Vehiclemodel=models.CharField(max_length=20,null=True)
   Purpose=models.CharField(max_length=20,null=True)
   Day=models.CharField(max_length=10,null=True)
   Status=models.IntegerField(default=0)
   moreinfo=models.TextField(default="No Data")


   



# ==============================End Package Management====================================






class SeekerComplaint(models.Model):
   SeekerID=models.ForeignKey(NewSeeker,on_delete=models.CASCADE)
   ComplaintType=models.ForeignKey(ComplaintType,on_delete=models.CASCADE)
   ComplaintTitle=models.CharField(max_length=50,null=False)
   ComplaintDetails=models.CharField(max_length=200,null=False)
   Reply=models.CharField(max_length=200,null=False,default=None)
   Status=models.CharField(max_length=10,null=False,default=None)
   ComplaintDate=models.DateTimeField(null=False,auto_now_add=True)