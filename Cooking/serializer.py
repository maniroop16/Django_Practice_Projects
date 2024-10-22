from rest_framework.serializers import ModelSerializer
from Cooking.models import *

class Addressserializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"