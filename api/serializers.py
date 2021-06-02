from django.db.models.base import ModelState

from core.models import Item
from rest_framework import serializers
from django.contrib.auth.models import User



from rest_framework import serializers



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'title',
            'price',
            'discount_price',

            'category',
            'label',
            'slug',
            'description',
            'image',
            'imageslide',
        )



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

