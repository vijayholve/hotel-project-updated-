from rest_framework.serializers import ModelSerializer
from base.models import restaurants,dish

class serializer_restaurant(ModelSerializer):
    class Meta:
        model=restaurants
        fields="__all__"
class serializer_dish(ModelSerializer):
    class Meta:
        model=dish
        fields="__all__"

class serializer_restaurant_dish(ModelSerializer):
    model=restaurants
     = models.FileField(upload_to=None, max_length = 100)
    
