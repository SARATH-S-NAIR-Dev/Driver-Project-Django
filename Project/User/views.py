from Seeker.views import SeekerPackage, seekercomplaint
from Seeker.models import *
from django.shortcuts import redirect, render
from Guest.models import NewSeeker, NewUser
import datetime
from BasicEntry.models import *
from .models import *

# Create your views here.

def homepage(request):
    return render(request,"User/Homepage.html",{})


def viewprofile(request):
    if request.session.has_key("userid"):
        userData=NewUser.objects.get(id=request.session["userid"])
        return render(request,"User/MyProfile.html",{"userData":userData})
    else:
        print("No Session")


def editprofile(request):
    if request.session.has_key("userid"):
        userData=NewUser.objects.get(id=request.session["userid"])
        if request.method=='POST':
            userData.UserPhone=request.POST.get("txtUserPhone")
            userData.UserEmail=request.POST.get("txtUserEmail")
            userData.save()
            return redirect("user:user-viewprofile")   
        else:
            return render(request,"User/EditProfile.html",{"userData":userData})    
    else:
        print("No Session")


def changepassword(request):
    if request.session.has_key("userid"):
        userData=NewUser.objects.get(id=request.session["userid"])
        oldPassword=request.POST.get("txtOldpassword")
        newPassword=request.POST.get("txtNewpassword")
        rePassword=request.POST.get("txtRepassword")
        if request.method=='POST':
            if oldPassword==userData.UserPassword:
                if newPassword==rePassword:
                    userData.UserPassword=newPassword
                    userData.save()
                    return redirect("user:user-homepage")
            else:
                return render(request,"User/ChangePassword.html",{})
        else:
            return render(request,"User/ChangePassword.html",{})
    else:
        print("No Session")

def usercomplaint(request):
    if request.session.has_key("userid"):
        complaint=ComplaintType.objects.all()
        if request.method=='POST':
            comptype_id=request.POST.get("slctComplaint")
            comptype=ComplaintType.objects.get(id=comptype_id)
            user=NewUser.objects.get(id=request.session["userid"])
            UserComplaint.objects.create(UserID=user,ComplaintType=comptype,ComplaintTitle=request.POST.get('txtComplaint'),ComplaintDetails=request.POST.get('txtareaComplaint'))
            
        else:
            return render(request,'User/UserComplaint.html',{'complaint':complaint})

def load_vehiclemodel(request):
    vechicleTypes =list(request.GET.get('vehtype'))
    # print("Data",vechicleTypes)
    vehmodel = VehicleModel.objects.filter(VehicleTypes__in=vechicleTypes)
    # print(vehmodel)
    return render(request,'Seeker/VehicleModel_dropdown_list.html', {'vehmodel':vehmodel})

# ==========================================================================================================================


# ==============Searching Funcationalitieesss=====================

from django.db.models import Q



def searchPackage(request):

    district=District.objects.all();
    vehicleType=VehicleType.objects.all()
    vechiclePackagePurposes=PackageTravelingPurpose.objects.all()
    drivingHours=DriveHour.objects.all()
    drivingMode=DriveMode.objects.all()


    if request.method=="POST":
        selectedDistrict=request.POST.get("slctDistrict")
        selectedVehicleModel=request.POST.get("slctVehicleModel")
        selectedPackagePurpose=request.POST.get("slctPackPurposes")
        selectedDrivingHours=request.POST.get("slctDrivingHours")
        seletedDrivingModes=request.POST.get("slctDrivingModes")
        packageStartDate=request.POST.get("txtFromDate")
        packageEndDate=request.POST.get("txtToDate")
        packageStartTime=request.POST.get("txtFromTime")
        packageEndTime=request.POST.get("txtToTime")

        DriversData=SeekerProfilePackage.objects.all()

        if(selectedDistrict!="0" ):
            DriversData = SeekerProfilePackage.objects.filter(SeekerID__District=selectedDistrict)
            print("DriversData1",DriversData)
        
        if(seletedDrivingModes!="0"):
            print(seletedDrivingModes)
            DriversData = DriversData.filter(PackageDrivingMode=seletedDrivingModes)
            print("DriversData2",DriversData)
        
        if(selectedDrivingHours!="0"):
            DriversData = DriversData.filter(PackageDrivingHours=selectedDrivingHours)
            print("DriversData3",DriversData)

        if(selectedVehicleModel!='0'):
            DriversData=DriversData.filter(packagevehiclemodels=selectedVehicleModel)
            print("DriversData4",DriversData)
        if(selectedPackagePurpose!='0'):
            DriversData=DriversData.filter(packagepurposes=selectedPackagePurpose)
            print("DriversData5",DriversData)
        
        
        return render(
                    request,
                    "User/SearchPackage.html",
                    {"district":district,
                     "vehicletype":vehicleType,
                     "packagepurposes":vechiclePackagePurposes,
                     "drivingHours":drivingHours,
                     "drivingMode":drivingMode,
                     "driversDetails":DriversData}
                    )     
    else:
        return render(
                    request,
                    "User/SearchPackage.html",
                    {"district":district,
                     "vehicletype":vehicleType,
                     "packagepurposes":vechiclePackagePurposes,
                     "drivingHours":drivingHours,
                     "drivingMode":drivingMode}
                    )



def searchShortDrive(request):
    
    district=District.objects.all();
    vehicleType=VehicleType.objects.all()
    vechicleShortDrivePurposes=ShortTravelingPurpose.objects.all()
    drivingHours=DriveHour.objects.all()
    drivingMode=DriveMode.objects.all()


    if request.method=="POST":
        selectedDistrict=request.POST.get("slctDistrict")
        selectedVehicleModel=request.POST.get("slctVehicleModel")
        selectedPackagePurpose=request.POST.get("slctPackPurposes")
        selectedDrivingHours=request.POST.get("slctDrivingHours")
        seletedDrivingModes=request.POST.get("slctDrivingModes")
        packageStartDate=request.POST.get("txtFromDate")
        packageEndDate=request.POST.get("txtToDate")
        packageStartTime=request.POST.get("txtFromTime")
        packageEndTime=request.POST.get("txtToTime")

        DriversData=SeekerProfileShortDrive.objects.all()

        if(selectedDistrict!="0" ):
            DriversData = SeekerProfileShortDrive.objects.filter(SeekerID__District=selectedDistrict)
            print("DriversData1",DriversData)
        
        if(seletedDrivingModes!="0"):
            print(seletedDrivingModes)
            DriversData = DriversData.filter(ShortDriveDrivingMode=seletedDrivingModes)
            print("DriversData2",DriversData)
        
        if(selectedDrivingHours!="0"):
            DriversData = DriversData.filter(ShortDriveDrivingHours=selectedDrivingHours)
            print("DriversData3",DriversData)

        if(selectedVehicleModel!='0'):
            DriversData=DriversData.filter(shortdrivevehiclemodels=selectedVehicleModel)
            print("DriversData4",DriversData)
        if(selectedPackagePurpose!='0'):
            DriversData=DriversData.filter(shortdrivepurposes=selectedPackagePurpose)
            print("DriversData5",DriversData)
        
        
        return render(
                    request,
                    "User/SearchShortDrive.html",
                    {"district":district,
                     "vehicletype":vehicleType,
                     "shortdrivepurposes":vechicleShortDrivePurposes,
                     "drivingHours":drivingHours,
                     "drivingMode":drivingMode,
                     "driversDetails":DriversData}
                    )     
    else:
        return render(
                    request,
                    "User/SearchShortDrive.html",
                    {"district":district,
                     "vehicletype":vehicleType,
                     "shortdrivepurposes":vechicleShortDrivePurposes,
                     "drivingHours":drivingHours,
                     "drivingMode":drivingMode}
                    )


def SearchLongdrive(request):

    district=District.objects.all();
    vehicleType=VehicleType.objects.all()
    vechiclePackagePurposes=PackageTravelingPurpose.objects.all()
    drivingHours=DriveHour.objects.all()
    drivingMode=DriveMode.objects.all()


    if request.method=="POST":
        selectedDistrict=request.POST.get("slctDistrict")
        selectedVehicleModel=request.POST.get("slctVehicleModel")
        selectedPackagePurpose=request.POST.get("slctPackPurposes")
        selectedDrivingHours=request.POST.get("slctDrivingHours")
        seletedDrivingModes=request.POST.get("slctDrivingModes")
        packageStartDate=request.POST.get("txtFromDate")
        packageEndDate=request.POST.get("txtToDate")
        packageStartTime=request.POST.get("txtFromTime")
        packageEndTime=request.POST.get("txtToTime")

        DriversData=SeekerProfileLongDrive.objects.all()

        if(selectedDistrict!="0" ):
            DriversData = SeekerProfileLongDrive.objects.filter(SeekerID__District=selectedDistrict)
            print("DriversData1",DriversData)
        
        if(seletedDrivingModes!="0"):
            print(seletedDrivingModes)
            DriversData = DriversData.filter(PackageDrivingMode=seletedDrivingModes)
            print("DriversData2",DriversData)
        
        if(selectedDrivingHours!="0"):
            DriversData = DriversData.filter(PackageDrivingHours=selectedDrivingHours)
            print("DriversData3",DriversData)

        if(selectedVehicleModel!='0'):
            DriversData=DriversData.filter(packagevehiclemodels=selectedVehicleModel)
            print("DriversData4",DriversData)
        if(selectedPackagePurpose!='0'):
            DriversData=DriversData.filter(packagepurposes=selectedPackagePurpose)
            print("DriversData5",DriversData)
        
        
        return render(
                    request,
                    "User/SearchLongDrive.html",
                    {"district":district,
                     "vehicletype":vehicleType,
                     "packagepurposes":vechiclePackagePurposes,
                     "drivingHours":drivingHours,
                     "drivingMode":drivingMode,
                     "driversDetails":DriversData}
                    )     
    else:
        return render(
                    request,
                    "User/SearchLongDrive.html",
                    {"district":district,
                     "vehicletype":vehicleType,
                     "packagepurposes":vechiclePackagePurposes,
                     "drivingHours":drivingHours,
                     "drivingMode":drivingMode}
                    )






# ====================================Booking Funcationalitty==========================================================                    



# Package Booking Section Start
def BookPackage(request,pk):
    package=SeekerProfilePackage.objects.get(id=pk)
    workdays=PackageWorkingdays.objects.filter(SeekerPackage=pk)
    models=PackageVehicleModels.objects.filter(SeekerPackage=pk)
    purposes=PackagePurposes.objects.filter(SeekerPackage=pk)
    
    
    if request.method=='POST':
        fromdate=request.POST.get("txtFromDate")
        todate=request.POST.get("txtToDate")
        picktime=request.POST.get("txtPicktime")
        droptime=request.POST.get("txtDroptime")
        vehiclemodel=request.POST.get("txtVehiclemodel")
        purpose=request.POST.get("txtPurpose")
        day=request.POST.get("rdbDay")
        moreInfo=request.POST.get("txtDescription")
        
        
        amount=package.PackageAmount
        fromdate1 = datetime.datetime.strptime(fromdate, "%Y-%m-%d").date()
        todate1 = datetime.datetime.strptime(todate, "%Y-%m-%d").date()
        x=  (todate1-fromdate1).days
        totalamount=int(amount)*x
        
        
        userobj=NewUser.objects.get(id=request.session["userid"])
        PackageBooking.objects.create(SeekerPackage=package,
                                        UserID=userobj,
                                        Fromdate=fromdate,
                                        Todate=todate,
                                        TotalAmount=totalamount,
                                        Picktime=picktime,
                                        Droptime=droptime,
                                        Vehiclemodel=vehiclemodel,
                                        Purpose=purpose,
                                        Day=day,
                                        moreinfo=moreInfo
                                        )

        return redirect('/user/searchpackage/')
    else:
        return render(request,"User/BookPackage.html",{'package':package,'workdays':workdays,'models':models,'purposes':purposes})

#Package Booking Section Ended



#Short Drive Boking Section Started


def BookShortDrive(request,pk):
    shortdrive=SeekerProfileShortDrive.objects.get(id=pk)
    workdays=ShortDriveWorkingdays.objects.filter(SeekerShortDrive=pk)
    models=ShortDriveVehicleModels.objects.filter(SeekerShortDrive=pk)
    purposes=ShortDrivePurposes.objects.filter(SeekerShortDrive=pk)
    moreInfo=request.POST.get("txtDescription")
    
    if request.method=='POST':
        
        
        amount=shortdrive.ShortDriveAmount
        
        
        
        userobj=NewUser.objects.get(id=request.session["userid"])
        ShortDriverBooking.objects.create(SeekerShortDriveid=shortdrive,
                                        UserID=userobj,
                                        ShortDriveBookingPickingDate=request.POST.get("txtDate"),
                                        ShortDriveBookingPickingTime=request.POST.get("txtPicktime"),
                                        ShortDriveBookingDropingTime=request.POST.get("txtDroptime"),
                                        ShortDriveBookingPickingLocation=request.POST.get("txtPickLocation"),
                                        ShortDriveBookingDropLocation=request.POST.get("txtDropLocation"),
                                        ShortDriveBookingIsReturn=request.POST.get("chkreturn"),
                                        ShortDrivePurpose=request.POST.get("txtPurpose"),
                                        ShortDriveVehicleModel=request.POST.get("txtVehiclemodel"),
                                        ShortDriveBookingAmount=amount,
                                        moreinfo=moreInfo
                                        )

        return redirect('/user/searchshortdrive/')
    else:
        return render(request,"User/BookShortDrive.html",{'shortdrive':shortdrive,'workdays':workdays,'models':models,'purposes':purposes})

#Short Drive Boking Section End


#Long Drive Boking Section start

def BookLongDrive(request,pk):
    longdrive=SeekerProfileLongDrive.objects.get(id=pk)
    workdays=LongDriveWorkingdays.objects.filter(SeekerLongDrive=pk)
    models=LongDriveVehicleModels.objects.filter(SeekerLongDrive=pk)
    purposes=LongDrivePurposes.objects.filter(SeekerLongDrive=pk)
    district=District.objects.all()
    if request.method=='POST':
        amount=longdrive.LongDriveAmount
        userobj=NewUser.objects.get(id=request.session["userid"])
        dist_id=request.POST.get("district")
        distobj=District.objects.get(id=dist_id)
        
        LongDriverBooking.objects.create(SeekerLongdrive=longdrive,
                                        UserID=userobj,
                                        LongDriveDistrictID=distobj,
                                        LongDriveLocation=request.POST.get("txtLocation"),
                                        LongDriveStartDate=request.POST.get("txtStartdate"),
                                        LongDriveStartTime=request.POST.get("txtStarttime"),
                                        LongDriveEndDate=request.POST.get("txtEnddate"),
                                        LongDriveEndTime=request.POST.get("txtEndtime"),
                                        LongDrivePurpose=request.POST.get("txtPurpose"),
                                        LongDriveVehicleModel=request.POST.get("txtVehiclemodel"),
                                        LongDriveBookingAmount=amount
                                        )

        return redirect('/user/searchlongdrive/')
    else:
        return render(request,"User/BookLongDrive.html",{'longdrive':longdrive,'workdays':workdays,'models':models,'purposes':purposes,'district':district})



#view booked details

def BookedPackages(request):
    package=PackageBooking.objects.filter(UserID=request.session["userid"])
    return render(request,"User/PackageBooked.html",{'packages':package})

def ShortDriveBooked(request):
    shortdrive=ShortDriverBooking.objects.filter(UserID=request.session["userid"])
    return render(request,"User/ShortDriveBooked.html",{'shortdrive':shortdrive})

def LongDriveBooked(request):
    longdrive=LongDriverBooking.objects.filter(UserID=request.session["userid"])
    return render(request,"User/LongDriveBooked.html",{'longdrive':longdrive})

#booked details view end

