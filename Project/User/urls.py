from django.urls.conf import path
from User import views

app_name="user"
urlpatterns= [
    path('homepage/',views.homepage,name="user-homepage"),
    path('viewprofile/',views.viewprofile,name="user-viewprofile"),
    path('editprofile/',views.editprofile,name="user-editprofile"),
    path('changepassword/',views.changepassword,name="user-changepassword"),
    path('usercomplaint/',views.usercomplaint,name="user-complaint"),   
    
    path('searchpackage/',views.searchPackage,name="search-package"),
    path('searchshortdrive/',views.searchShortDrive,name="search-short-drive"),
    path('searchlongdrive/',views.SearchLongdrive,name="search-long-drive"),
    
    path('bookpackage/<int:pk>',views.BookPackage,name="book-package"),
    path('bookshortdrive/<int:pk>',views.BookShortDrive,name="book-short-drive"),
    path('booklongdrive/<int:pk>',views.BookLongDrive,name="book-long-drive"),

    path('packagebooked/',views.BookedPackages,name="package-booked"),
    path('shortdrivebooked/',views.ShortDriveBooked,name="short-drive-booked"),
    path('longdrivebooked/',views.LongDriveBooked,name="long-drive-booked"),

    
    
    path('ajax/load-vehiclemodel/', views.load_vehiclemodel,name="ajax_load_vehmodel"),

]