from django.urls.conf import path
from Seeker import views

app_name="seeker"
urlpatterns= [
    path('homepage/',views.homepage,name="seeker-homepage"),
    path('viewprofile/',views.viewprofile,name="seeker-viewprofile"),
    path('editprofile/',views.editprofile,name="seeker-editprofile"),
    path('changepassword/',views.changepassword,name="seeker-changepassword"),
    
    path('seekerregistration/',views.seekerregistration,name="seeker-registration"),
    path('seekertest/',views.seekertest,name="seeker-test"),
    
    path('seekershortdrive/',views.SeekerShortDrive,name="seeker-shortdrive"),
    path('seekerlongdrive/',views.SeekerLongDrive,name="seeker-longdrive"),
    path('seekerpackage/',views.SeekerPackage,name="seeker-package"),
    
    path('viewpackage/',views.BookedPackage,name="booked-package"),
    path('acceptpackage/<int:pk>',views.AcceptPackage,name="accept-package"),
    
    path('viewshortdrive/',views.BookedShortDrive,name="booked-short-drive"),
    path('acceptshortdrive/<int:pk>',views.AcceptShortDrive,name="accept-shortdrive"),

    path('viewlongdrive/',views.BookedLongDrive,name="booked-long-drive"),
    path('acceptlongdrive/<int:pk>',views.AcceptLongtDrive,name="accept-longdrive"),
    
    path('seekercomplaint/',views.seekercomplaint,name="seeker-complaint"),
    path('ajax/load-vehiclemodel/', views.load_vehiclemodel,name="ajax_load_vehmodel"),
    
    path('shortdrivecompleted/<int:pk>/', views.shortdrivecompleted,name="shortdrive-completed"),
    path('longdrivecompleted/<int:pk>/', views.longdrivecompleted,name="longdrive-completed"),
]

