from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile
from rooms.models import Room,Booking 
from base.models import orders    
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
@login_required(login_url="login-page")
def User_profile_fun(request,pk):
    user=User.objects.get(id=pk)
    restaurant=user.restaurants_set.all()
    bookeds=user.booking_set.all()
    rooms=user.room_set.all()
    orders=user.orders_set.all()
    if user.userprofile:
        profile=user.userprofile
    content={"user":user,"profile":profile,"restaurant":restaurant,"booked":bookeds,
             "rooms":rooms,"orders":orders}
    return render(request,"accounts/userProfile.html",content)
def update_profile(request,pk):
    profile=UserProfile.objects.get(id=pk)
    if request.method == "POST":
        
        return _extracted_from_update_profile_5(request, profile)
    content={"profile":profile}
    return render(request,"accounts/update_profile.html",content)


# TODO Rename this here and in `update_profile`
def _extracted_from_update_profile_5(request, profile):
    username=request.POST.get("username")
    city=request.POST.get("city")
    ProfilePicture=request.FILES.get("image")
    dob=request.POST.get("dob")

    if ProfilePicture:
        profile.profilePicture=ProfilePicture
    if dob:
        profile.dateOfBirth=dob
    profile.city=city
    profile.user.username=username
    profile.save()
    return  redirect("profile",pk=profile.user.id)

def create_profile(request):
    users=User.objects.all()
    if request.method == "POST":
        return _extracted_from_create_profile_6(request, users)
    content={"users":users}
    return render(request,"accounts/createprofile.html",content)    
def _extracted_from_create_profile_6(request,users):
    
    city=request.POST.get("city")
    ProfilePicture=request.FILES.get("image")
    dob=request.POST.get("dob")
    user=request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    profile.profilePicture = ProfilePicture
    profile.dateOfBirth = dob
    profile.city = city
    profile.save()
    # if ProfilePicture:
    #     profile.profilePicture=ProfilePicture
    # if dob:
    #     profile.dateOfBirth=dob
    # profile.city=city
    # user=request.user
    profile.save()
    return  redirect("profile",pk=profile.user.id)

@login_required(login_url="login-page")
def user_rooms_data(request,pk):
    bookings = Booking.objects.filter(user_id=pk).select_related('room')
    rooms = {booking.room for booking in bookings}
    profile=UserProfile.objects.get(user__id=pk)
    
    context = {
        'rooms': rooms,
        "profile":profile
    }
    return render(request,"room/booking_data.html",context)
@login_required(login_url="login-page")   
def user_dish_data(request,pk):
    user=User.objects.get(id=pk)
    order=orders.objects.filter(user=user)
    dishes={o.dish for o in order}
    sum_order={}
    for d in dishes:
        KeyError at /profile/user-dishes/51/
994
Request Method:	GET
Request URL:	http://127.0.0.1:8000/profile/user-dishes/51/
Django Version:	5.0.6
Exception Type:	KeyError
Exception Value:	
994
Exception Location:	C:\Users\Vijay\django_pro\hotels\accounts\views.py, line 90, in user_dish_data
Raised during:	accounts.views.user_dish_data
Python Executable:	C:\Users\Vijay\django_pro\hotels\myenv\scripts\python.exe
Python Version:	3.12.3
Python Path:	
['C:\\Users\\Vijay\\django_pro\\hotels',
 'C:\\Users\\Vijay\\django_pro\\hotels',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312\\Lib',
 'C:\\Users\\Vijay\\AppData\\Local\\Programs\\Python\\Python312',
 'C:\\Users\\Vijay\\django_pro\\hotels\\myenv',
 'C:\\Users\\Vijay\\django_pro\\hotels\\myenv\\Lib\\site-packages',
 'C:\\Users\\Vijay\\django_pro\\hotels\\myenv\\Lib\\site-packages\\win32',
 'C:\\Users\\Vijay\\django_pro\\hotels\\myenv\\Lib\\site-packages\\win32\\lib',
 'C:\\Users\\Vijay\\django_pro\\hotels\\myenv\\Lib\\site-packages\\Pythonwin']
Server time:	Wed, 26 Jun 2024 14:31:45 +0000
Traceback Switch to copy-and-paste view
C:\Users\Vijay\django_pro\hotels\myenv\Lib\site-packages\django\core\handlers\exception.py, line 55, in inner
                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\django_pro\hotels\myenv\Lib\site-packages\django\core\handlers\base.py, line 197, in _get_response
                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\django_pro\hotels\myenv\Lib\site-packages\django\contrib\auth\decorators.py, line 23, in _wrapper_view
                return view_func(request, *args, **kwargs)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\Vijay\django_pro\hotels\accounts\views.py, line 90, in user_dish_data
@login_required(login_url="login-page")   
def user_dish_data(request,pk):
    user=User.objects.get(id=pk)
    order=orders.objects.filter(user=user)
    dishes={o.dish for o in order}
    sum_order={}
    for d in dishes:
        sum_order[d.id]+=order.filter(dish=d).aggregate(Sum('total_charges'))
            ^^^^^^^^^^^^^^^ …
        
    profile=user.userprofile
    
    content={"dishes":dishes,
             "profile":profile}
    return render(request,"restaurant/dishes_data_user.html",content)
        
    profile=user.userprofile
    
    content={"dishes":dishes,
             "profile":profile}
    return render(request,"restaurant/dishes_data_user.html",content)
    