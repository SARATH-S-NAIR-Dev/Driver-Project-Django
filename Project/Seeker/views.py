from django.shortcuts import redirect, render
from Guest.models import NewSeeker
from Seeker.models import *
from BasicEntry.models import *

# Create your views here.

def homepage(request):
    seeker = request.session["seekerid"]
    return render(request,"Seeker/Homepage.html",{'seeker':seeker})


def viewprofile(request):
    if request.session.has_key("seekerid"):
        seekerData=NewSeeker.objects.get(id=request.session["seekerid"])
        return render(request,"Seeker/MyProfile.html",{"seekerData":seekerData})
    else:
        print("No Session")


def editprofile(request):
    if request.session.has_key("seekerid"):
        seekerData=NewSeeker.objects.get(id=request.session["seekerid"])
        if request.method=='POST':
            # print(request.session["seekerid"])
            seekerData.SeekerPhone=request.POST.get("txtSeekerPhone")
            seekerData.SeekerEmail=request.POST.get("txtSeekerEmail")
            seekerData.save()
            return redirect("seeker:seeker-viewprofile")
        else:
            return render(request,"Seeker/EditProfile.html",{"seekerData":seekerData})    
    else:
        print("No Session")


def changepassword(request):
    if request.session.has_key("seekerid"):
        seekerData=NewSeeker.objects.get(id=request.session["seekerid"])
        oldPassword=request.POST.get("txtOldpassword")
        newPassword=request.POST.get("txtNewpassword")
        rePassword=request.POST.get("txtRepassword")
        if request.method=='POST':
            if oldPassword==seekerData.SeekerPassword:
                if newPassword==rePassword:
                    seekerData.SeekerPassword=newPassword
                    seekerData.save()
                    return redirect("seeker:seeker-homepage")
            else:
                return render(request,"Seeker/ChangePassword.html",{})
        else:
            return render(request,"Seeker/ChangePassword.html",{})
    else:
        print("No Session")


def seekerregistration(request):
    if request.session.has_key("seekerid"):
        StatusObj=NewSeeker.objects.get(id=request.session["seekerid"])
        if request.method=="POST":
            SeekerObj=SeekerRegistration()
            SeekerObj.SeekerLicenseNumber=request.POST.get("txtLicense")
            SeekerObj.SeekerLicenseProof=request.FILES.get("fileLicense")
            SeekerObj.SeekerAadharNumber=request.POST.get("txtAadhar")
            SeekerObj.SeekerAadharProof=request.FILES.get("fileLicense")
            SeekerObj.SeekerEyeTest=request.FILES.get("fileEyeTest")
            SeekerObj.SeekerAdress=request.POST.get("txtAddress")
            SeekerObj.SeekerDisability=request.POST.get("txtDisability")
            SeekerObj.SeekerDisabilityProof=request.FILES.get("fileDisability")
            SeekerObj.SeekerBadge=request.POST.get("txtBadge")
            SeekerObj.SeekerBadgeProof=request.FILES.get("fileBadge")
            SeekerObj.SeekerOffence=request.POST.get("txtOffence")
            SeekerObj.SeekerRestriction=request.POST.get("txtRestrictions")
            SeekerObj.SeekerID=StatusObj
            SeekerObj.save()
            StatusObj.PersonaldataStatus="1"
            StatusObj.save()
            return redirect("seeker:seeker-test")
        else:
            return render(request,"Seeker/SeekerRegistration.html",{})
    else:
        print("No Session")



def seekertest(request):
    if request.session.has_key("seekerid"):
        allQuestions=SeekerTestQuestion.objects.all()
        seekerData=NewSeeker.objects.get(id=request.session["seekerid"])
        data="Success!!!"
        if request.method=="POST":
            for qdata in allQuestions:
                optionname="rdbOption"+str(qdata.id)
                questionID=qdata.id
                questionData=SeekerTestQuestion.objects.get(id=questionID)
                selectedoption=request.POST.get(optionname)
                SeekerTestObj=SeekerTest()
                SeekerTestObj.SeekerID=seekerData
                SeekerTestObj.TestQuestion=questionData
                SeekerTestObj.TestAnswer=selectedoption
                SeekerTestObj.save()
                StatusObj=NewSeeker.objects.get(id=request.session["seekerid"])
                StatusObj.TestdataStatus="1"
                StatusObj.save()
            return render(request,"Seeker/SeekerTest.html",{"allQuestions":allQuestions,"data":data})
        else:
            return render(request,"Seeker/SeekerTest.html",{"allQuestions":allQuestions})
    else:
        print("No Session")

def load_vehiclemodel(request):
    vechicleTypes =list(request.GET.get('vehtype'))
    # print("Data",vechicleTypes)
    vehmodel = VehicleModel.objects.filter(VehicleTypes__in=vechicleTypes)
    # print(vehmodel)
    return render(request,'Seeker/VehicleModel_dropdown_list.html', {'vehmodel':vehmodel})

    
def SeekerShortDrive(request):
    seeker=NewSeeker.objects.get(id=request.session["seekerid"])
    vehicletype=VehicleType.objects.all()
    vehiclemodel=VehicleModel.objects.all()
    drivemode=DriveMode.objects.all()
    drivehrs=DriveHour.objects.all()
    workday=Weekday.objects.all()
    shortpurpose=ShortTravelingPurpose.objects.all()
    shortdrive=SeekerProfileShortDrive.objects.all()
    print("Shot Drive Data",shortdrive)

    if request.method=='POST':
        SeekerProfileShortDrive.objects.create(
                SeekerID=seeker,
                ShortDriveDrivingMode=DriveMode.objects.get(id=request.POST.get('drivemode')),
                ShortDriveDrivingHours=DriveHour.objects.get(id=request.POST.get('drivehrs')),
                ShortDriveEligibility=request.POST.get('eligibility'),
                ShortDriveAmount=request.POST.get('amount') 
        )
                
        weekdays=request.POST.getlist('chk')
        vehiclemodels=request.POST.getlist("vehmodel-list[]")
        purposes=request.POST.getlist('purpose_list')
        shortseekerobj=SeekerProfileShortDrive.objects.last()
        
        
        for data in weekdays:
            weekobj=Weekday.objects.get(id=data)
            ShortDriveWorkingdays.objects.create(SeekerShortDrive=shortseekerobj,WorkingDays=weekobj)
        
        
        for vdata in vehiclemodels:
            print("SeekerObj",shortseekerobj)
            vehiclemodelobj=VehicleModel.objects.get(id=vdata)
            ShortDriveVehicleModels.objects.create(SeekerShortDrive=shortseekerobj,VehicleModel=vehiclemodelobj)

        for pdata in purposes:
            purposeobj=ShortTravelingPurpose.objects.get(id=pdata)
            ShortDrivePurposes.objects.create(SeekerShortDrive=shortseekerobj,Purposes=purposeobj)
        
        
        shortdrive=SeekerProfileShortDrive.objects.all()
        return render(request,
                        'Seeker/ShortDriveProfile.html',
                        {'vehiclemodel':vehiclemodel,
                        'drivemode':drivemode,
                        'drivehrs':drivehrs,
                        'workday':workday,
                        'shortpurpose':shortpurpose,
                        'vehicletype':vehicletype,
                        'shortdrive':shortdrive})
    else:
        shortdrive=SeekerProfileShortDrive.objects.all()
        return render(request,
                        'Seeker/ShortDriveProfile.html',
                        {'vehiclemodel':vehiclemodel,
                        'drivemode':drivemode,
                        'drivehrs':drivehrs,
                        'workday':workday,
                        'shortpurpose':shortpurpose,
                        'vehicletype':vehicletype,
                        'shortdrive':shortdrive})

                                    
def SeekerLongDrive(request):
    seeker=NewSeeker.objects.get(id=request.session["seekerid"])
    vehicletype=VehicleType.objects.all()
    vehiclemodel=VehicleModel.objects.all()
    drivemode=DriveMode.objects.all()
    drivehrs=DriveHour.objects.all()
    workday=Weekday.objects.all()
    longpurpose=LongTravelingPurpose.objects.all()

    if request.method=='POST':
        SeekerProfileLongDrive.objects.create(
                SeekerID=seeker,
                LongDriveDrivingMode=DriveMode.objects.get(id=request.POST.get('drivemode')),
                LongDriveDrivingHours=DriveHour.objects.get(id=request.POST.get('drivehrs')),
                LongDriveEligibility=request.POST.get('eligibility'),
                LongDriveAmount=request.POST.get('amount') 
        )
                
        weekdays=request.POST.getlist('chk')
        vehiclemodels=request.POST.getlist("vehmodel-list[]")
        purposes=request.POST.getlist('purpose_list')
        longseekerobj=SeekerProfileLongDrive.objects.last()
        
        
        for data in weekdays:
            weekobj=Weekday.objects.get(id=data)
            LongDriveWorkingdays.objects.create(SeekerLongDrive=longseekerobj,WorkingDays=weekobj)
        
        
        for vdata in vehiclemodels:
            vehiclemodelobj=VehicleModel.objects.get(id=vdata)
            LongDriveVehicleModels.objects.create(SeekerLongDrive=longseekerobj,VehicleModel=vehiclemodelobj)

        for pdata in purposes:
            purposeobj=LongTravelingPurpose.objects.get(id=pdata)
            LongDrivePurposes.objects.create(SeekerLongDrive=longseekerobj,Purposes=purposeobj)
        
        
        longdrive=SeekerProfileLongDrive.objects.all()
        return render(request,
                        'Seeker/LongDriveProfile.html',
                        {'vehiclemodel':vehiclemodel,
                        'drivemode':drivemode,
                        'drivehrs':drivehrs,
                        'workday':workday,
                        'longpurpose':longpurpose,
                        'vehicletype':vehicletype,
                        'longdrive':longdrive})
    else:
        longdrive=SeekerProfileLongDrive.objects.all()
        return render(request,
                        'Seeker/LongDriveProfile.html',
                        {'vehiclemodel':vehiclemodel,
                        'drivemode':drivemode,
                        'drivehrs':drivehrs,
                        'workday':workday,
                        'longpurpose':longpurpose,
                        'vehicletype':vehicletype,
                        'longdrive':longdrive})


def SeekerPackage(request):
    seeker=NewSeeker.objects.get(id=request.session["seekerid"])
    vehicletype=VehicleType.objects.all()
    vehiclemodel=VehicleModel.objects.all()
    drivemode=DriveMode.objects.all()
    drivehrs=DriveHour.objects.all()
    workday=Weekday.objects.all()
    packagepurpose=PackageTravelingPurpose.objects.all()

    if request.method=='POST':
        SeekerProfilePackage.objects.create(
                SeekerID=seeker,
                PackageDrivingMode=DriveMode.objects.get(id=request.POST.get('drivemode')),
                PackageDrivingHours=DriveHour.objects.get(id=request.POST.get('drivehrs')),
                PackageEligibility=request.POST.get('eligibility'),
                PackageAmount=request.POST.get('amount') 
        )
                
        weekdays=request.POST.getlist('chk')
        vehiclemodels=request.POST.getlist("vehmodel-list[]")
        purposes=request.POST.getlist('packagepurpose')
        print(purposes)
        packageobj=SeekerProfilePackage.objects.last()
        
        
        for data in weekdays:
            weekobj=Weekday.objects.get(id=data)
            PackageWorkingdays.objects.create(SeekerPackage=packageobj,WorkingDays=weekobj)
        
        
        for vdata in vehiclemodels:
            vehiclemodelobj=VehicleModel.objects.get(id=vdata)
            PackageVehicleModels.objects.create(SeekerPackage=packageobj,VehicleModel=vehiclemodelobj)

        for pdata in purposes:
            print("Data",pdata)
            purposeobj=PackageTravelingPurpose.objects.get(id=pdata)
            print("PurposeObject",purposeobj)
            PackagePurposes.objects.create(SeekerPackage=packageobj,Purposes=purposeobj)
        
        
        package=SeekerProfilePackage.objects.all()
        return render(request,
                    'Seeker/PackageProfile.html',
                    {'vehiclemodel':vehiclemodel,
                    'drivemode':drivemode,
                    'drivehrs':drivehrs,
                    'workday':workday,
                    'packagepurpose':packagepurpose,
                    'vehicletype':vehicletype,
                    'package':package})

    else:
        package=SeekerProfilePackage.objects.all()
        return render(request,
                        'Seeker/PackageProfile.html',
                        {'vehiclemodel':vehiclemodel,
                        'drivemode':drivemode,
                        'drivehrs':drivehrs,
                        'workday':workday,
                        'packagepurpose':packagepurpose,
                        'vehicletype':vehicletype,
                        'package':package})

def seekercomplaint(request):
    if request.session.has_key("seekerid"):
        complaint=ComplaintType.objects.all()
        seeker=NewSeeker.objects.get(id=request.session["seekerid"])
        if request.method=='POST':
            comp=request.POST.get("slctComplaint")
            compobj=ComplaintType.objects.get(id=comp)
            complaintObj=SeekerComplaint()
            complaintObj.SeekerID=seeker
            complaintObj.ComplaintType=compobj
            complaintObj.ComplaintTitle=request.POST.get("txtComplaint")
            complaintObj.ComplaintDetails=request.POST.get("txtareaComplaint")
            complaintObj.save()
            return redirect("seeker:seeker-homepage")
        else:
            return render(request,'Seeker/SeekerComplaint.html',{'complaint':complaint})
    
def BookedPackage(request):
    packages=PackageBooking.objects.filter(SeekerPackage__SeekerID=request.session["seekerid"])
    return render(request,"Seeker/BookedPackages.html",{'packages':packages})

def BookedShortDrive(request):
    shortdrive=ShortDriverBooking.objects.filter(SeekerShortDriveid__SeekerID=request.session["seekerid"])
    return render(request,"Seeker/BookedShortDrive.html",{'shortdrive':shortdrive})

def BookedLongDrive(request):
    longdrive=LongDriverBooking.objects.filter(SeekerLongdrive__SeekerID=request.session["seekerid"])
    return render(request,"Seeker/BookedLongDrive.html",{'longdrive':longdrive})

def AcceptPackage(request,pk):
    sel_package=PackageBooking.objects.get(id=pk)
    sel_package.Status=1
    sel_package.save()
    return redirect("seeker:booked-package")

def AcceptShortDrive(request,pk):
    sel_shortdrive=ShortDriverBooking.objects.get(id=pk)
    sel_shortdrive.Status=1
    sel_shortdrive.save()
    return redirect("seeker:booked-short-drive")

def AcceptLongtDrive(request,pk):
    sel_longdrive=LongDriverBooking.objects.get(id=pk)
    sel_longdrive.Status=1
    sel_longdrive.save()
    driverobj=NewSeeker.objects.get(id=request.session["seekerid"])
    driverobj.longdrivestatus=1
    driverobj.save()
    return redirect("seeker:booked-long-drive")

def shortdrivecompleted(request,pk):
    sel_shortdrive=ShortDriverBooking.objects.get(id=pk)
    if request.method=="POST":
        sel_shortdrive.actualtotalamount=request.POST.get("txtTotalAmount")
        sel_shortdrive.workcompletionremarks=request.POST.get("txtReamarks")
        sel_shortdrive.Status=2
        sel_shortdrive.save()
        return redirect("seeker:booked-short-drive")
        
    else:
        return render(request,"Seeker/CompleteShortDrive.html",{})

def longdrivecompleted(request,pk):
    sel_longdrive=LongDriverBooking.objects.get(id=pk)
    if request.method=="POST":
        sel_longdrive.actualtotalamount=request.POST.get("txtTotalAmount")
        sel_longdrive.workcompletionremarks=request.POST.get("txtReamarks")
        sel_longdrive.Status=2
        sel_longdrive.save()
        driverobj=NewSeeker.objects.get(id=request.session["seekerid"])
        driverobj.longdrivestatus=0
        driverobj.save()
        return redirect("seeker:booked-long-drive")
        
    else:
        return render(request,"Seeker/CompleteLongDrive.html",{})

