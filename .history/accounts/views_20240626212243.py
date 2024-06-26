from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile
from rooms.models import Room,Booking 
from base.models import orders    
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Avg
from django.template.defaulttags import register
from base.models import Reviews
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
    count_dish={}
    review_order={}
    for d in dishes:
        if d.id not in review_order:
            review_order[d.id]=0
        review_order[d.id]+=Reviews.objects.filter(dish=d).aggregate(Avg("review"))['review__avg']
    
    for d in dishes:
        if d.id not in sum_order:
            sum_order[d.id] = 0
        sum_order[d.id]+=order.filter(dish=d).aggregate(Sum("total_charges"))["total_charges__sum"] 
        if d.id not in count_dish:
            count_dish[d.id] = 0
        count_dish[d.id]+=order.filter(dish=d).count()
         
    profile=user.userprofile
    print("sum",sum_order)
    content={"dishes":dishes,
             "profile":profile,
             "sum_order":sum_order,
             "count_dish":count_dish,
             "reviews":review_order}
    return render(request,"restaurant/dishes_data_user.html",content)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)