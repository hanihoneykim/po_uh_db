from rest_framework import serializers
from .models import MyeongdongReservation


class MyeongdongReservationSerialzier(serializers.Serializer):
    class Meta:
        model = MyeongdongReservation
        fields = "__all__"
        read_only_fields = ("id",)
