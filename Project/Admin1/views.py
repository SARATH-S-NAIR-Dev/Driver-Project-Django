from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from BasicEntry.models import SeekerTestQuestion
from Guest.models import NewSeeker
from Seeker.models import SeekerRegistration, SeekerTest


# Create your views here.

def viewseekers(request):
    seekerData = NewSeeker.objects.all()
    return render(request, "Admin1/RegisteredSeeker.html", {"seekerData": seekerData})


def seekerregistrationdata(request, id):
    seekerData = NewSeeker.objects.get(id=id)
    seekerRegistrationdata = SeekerRegistration.objects.get(SeekerID=id)
    if request.method == "POST":
        seekerData.PersonaldataStatus = "2"
        seekerData.save()
        return redirect("webadmin:webadmin-viewseekers")
    else:
        return render(request, "Admin1/ViewSeekerRegistrationDetails.html",
                      {"seekerRegistrationdata": seekerRegistrationdata, "seekerData": seekerData})


def seekertestdata(request, id):
    attemptedQuestions = SeekerTest.objects.filter(SeekerID=id)
    seekerData = NewSeeker.objects.get(id=id)
    if request.method == "POST":
        seekerData.TestdataStatus = "2"
        seekerData.save()
        return redirect("webadmin:webadmin-viewseekers")
    else:
        return render(request, "Admin1/ViewSeekerTestDetails.html", {"attemptedQuestions": attemptedQuestions})
