from django.db import models


# Create your models here.

class District(models.Model):
    DistrictName = models.CharField(max_length=50)

    def __str__(self):
        return self.DistrictName


class Place(models.Model):
    PlaceName = models.CharField(max_length=50)
    DistrictName = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.PlaceName


class ComplaintType(models.Model):
    ComplaintTypeName = models.CharField(max_length=50, verbose_name="Complaint Type", unique=True)

    def __str__(self):
        return self.ComplaintTypeName


class RequestType(models.Model):
    RequestTypeName = models.CharField(max_length=50)

    def __str__(self):
        return self.RequestTypeName


class SeekerTestQuestion(models.Model):
    TestQuestions = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.TestQuestions


class ShortTravelingPurpose(models.Model):
    ShortTravelingPurposes = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.ShortTravelingPurposes


class LongTravelingPurpose(models.Model):
    LongTravelingPurposes = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.LongTravelingPurposes


class PackageTravelingPurpose(models.Model):
    PackageTravelingPurposes = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.PackageTravelingPurposes


class VehicleType(models.Model):
    VehicleTypes = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.VehicleTypes


class VehicleModel(models.Model):
    VehicleTypes = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    ModelName = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.ModelName


class DriveMode(models.Model):
    DriveModes = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.DriveModes


class Weekday(models.Model):
    Weeks = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.Weeks


class DriveHour(models.Model):
    Time = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.Time
