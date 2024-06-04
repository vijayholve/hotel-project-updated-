
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("base.urls")),
    path("profile/","")
    path("api/",include("api.urls")),
]