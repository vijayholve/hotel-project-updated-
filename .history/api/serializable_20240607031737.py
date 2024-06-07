from rest_framework.serializers import ModelSerializer
from base.models import restaurants,dish
from django.contrib.auth.models import User
class serializer_restaurant(ModelSerializer):
    dish=serializer_dish(many=False)
    class Meta:
        model=restaurants
        fields="__all__"
class serializer_dish(ModelSerializer):
    class Meta:
        model=dish
        fields="__all__"

    
class User_Serializar(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']