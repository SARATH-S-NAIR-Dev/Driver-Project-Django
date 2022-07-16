from django.urls.conf import path
from Admin1 import views

app_name="webadmin"
urlpatterns= [
    path('viewseekers/',views.viewseekers,name="webadmin-viewseekers"),
    path('view-registration-data/<int:id>/',views.seekerregistrationdata,name="view-registration-data"),
    path('view-test-data/<int:id>/',views.seekertestdata,name="view-test-data"),
]