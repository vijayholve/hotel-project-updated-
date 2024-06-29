from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture=models.ImageField(upload_to="accouts/",default=rf"images/default-avatar-profile-icon-social-media-user-image-gray-avatar-icon-blank-profile-silhouette-vector-illustration_561158-3383.avif",null=True,blank=True)
    dateOfBirth=models.DateField(null=True,blank=True)
    city=models.CharField(default="Pune",max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return self.user.username
    
    
    
     