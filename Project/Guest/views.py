from Admin1.models import WebAdmin
from django.shortcuts import get_object_or_404, redirect, render

from BasicEntry.models import District
from Guest.models import NewSeeker, NewUser


# Create your views here.
def LandingPage(request):
    return render(request,"Guest/index.html",{})
def NewUserEntry(request):
    distData=District.objects.all()
    if request.method=="POST":
        password=request.POST.get("txtPassword")
        repassword=request.POST.get("txtPassword")
        districtID=request.POST.get("slctDistrict")
        districtObj=District.objects.get(id=districtID)
        UserObj=NewUser()
        UserObj.UserName=request.POST.get("txtName")
        UserObj.UserGender=request.POST.get("txtGender")
        UserObj.UserPhone=request.POST.get("txtPhone")
        UserObj.UserEmail=request.POST.get("txtEmail")
        UserObj.District=districtObj
        UserObj.UserPassword=request.POST.get("txtPassword")
        if password==repassword:
            UserObj.save()
        return render(request,"Guest/NewUser.html",{"distData":distData})
    else:
        return render(request,"Guest/NewUser.html",{"distData":distData})

def NewSeekerEntry(request):
    distData=District.objects.all()
    if request.method=="POST":
        password=request.POST.get("txtPassword")
        repassword=request.POST.get("txtPassword")
        districtID=request.POST.get("slctDistrict")
        districtObj=District.objects.get(id=districtID)
        SeekerObj=NewSeeker()
        SeekerObj.SeekerName=request.POST.get("txtName")
        SeekerObj.SeekerGender=request.POST.get("txtGender")
        SeekerObj.SeekerDob=request.POST.get("txtDob")
        SeekerObj.SeekerPhone=request.POST.get("txtPhone")
        SeekerObj.SeekerEmail=request.POST.get("txtEmail")
        SeekerObj.District=districtObj
        SeekerObj.SeekerPassword=request.POST.get("txtPassword")
        if password==repassword:
            SeekerObj.save()
        return render(request,"Guest/NewSeeker.html",{"distData":distData})
    else:
        return render(request,"Guest/NewSeeker.html",{"distData":distData})


def login(request):
        if request.method=='POST':
            Usercount=NewUser.objects.filter(UserEmail=request.POST.get("txtLoginEmail"),UserPassword=request.POST.get("txtLoginPassword")).count()
            Seekercount=NewSeeker.objects.filter(SeekerEmail=request.POST.get("txtLoginEmail"),SeekerPassword=request.POST.get("txtLoginPassword")).count()
            Admincount=WebAdmin.objects.filter(Username=request.POST.get("txtLoginEmail"),Password=request.POST.get("txtLoginPassword")).count()
            if Usercount>0:
                userobj = get_object_or_404(NewUser, UserEmail=request.POST.get("txtLoginEmail"),UserPassword=request.POST.get("txtLoginPassword"))
                request.session["userid"]=userobj.id
                return redirect("user:user-homepage")

            elif Seekercount>0:
                seekerobj = get_object_or_404(NewSeeker, SeekerEmail=request.POST.get("txtLoginEmail"),SeekerPassword=request.POST.get("txtLoginPassword"))
                request.session["seekerid"]=seekerobj.id
                return redirect("seeker:seeker-homepage")

            elif Admincount>0:
                adminobj = get_object_or_404(WebAdmin, Username=request.POST.get("txtLoginEmail"),Password=request.POST.get("txtLoginPassword"))
                request.session["adminid"]=adminobj.id
                return redirect("webadmin:webadmin-viewseekers")

            else:
                return render(request,"guest/Login.html")
            
        return render(request,"guest/Login.html",{})