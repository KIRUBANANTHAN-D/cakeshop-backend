from rest_framework import serializers
from .models import Cake, Order


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    cake_name = serializers.CharField(source="cake.name", read_only=True)

    class Meta:
        model = Order
        fields = "__all__"