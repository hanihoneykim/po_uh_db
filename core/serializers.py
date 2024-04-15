from rest_framework import serializers
from .models import Guest
from the_myeongdong.models import MyeongdongReservation


class GuestSerializer(serializers.ModelSerializer):
    visit_count = serializers.SerializerMethodField()

    class Meta:
        model = Guest
        fields = "__all__"
        read_only_fields = ("id",)

    def get_visit_count(self, obj):
        # MyeongdongReservation 모델에서 'guest_name'과 'phone_number'가 일치하는 항목들의 개수를 가져옵니다.
        visit_count = MyeongdongReservation.objects.filter(
            guest_name=obj.guest_name, phone_number=obj.phone_number
        ).count()
        return visit_count
