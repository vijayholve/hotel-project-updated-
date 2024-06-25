from django.urls import path,include
from . import views
urlpatterns = [
    path("<str:pk>/",views.User_profile_fun,name="profile"),
    path("profile-update/<str:pk>/",views.update_profile,name="profile-update"),
    path("user-room",views.user_rooms_data,name="user-rooms")
]
