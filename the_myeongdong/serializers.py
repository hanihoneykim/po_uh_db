from rest_framework import serializers
from .models import MyeongdongReservation
from django.utils import formats


class MyeongdongReservationSerializer(serializers.ModelSerializer):
    total_room_charge = serializers.SerializerMethodField()
    adr = serializers.SerializerMethodField()

    def add_commas(self, value):
        # 쉼표를 추가할 문자열로 변환
        value_str = str(value)
        # 소수점 위치 찾기
        decimal_index = value_str.find(".")
        if decimal_index == -1:
            # 소수점이 없으면 전체 길이에서 세 자리마다 쉼표 추가
            return ",".join(
                reversed(
                    [value_str[max(i - 3, 0) : i] for i in range(len(value_str), 0, -3)]
                )
            )
        else:
            # 소수점이 있는 경우, 소수점 이전의 숫자에만 쉼표 추가
            return (
                ",".join(
                    reversed(
                        [
                            value_str[max(i - 3, 0) : i]
                            for i in range(decimal_index, 0, -3)
                        ]
                    )
                )
                + value_str[decimal_index:]
            )

    def get_total_room_charge(self, obj):
        return self.add_commas(obj.total_room_charge)

    def get_adr(self, obj):
        return self.add_commas(obj.adr)

    class Meta:
        model = MyeongdongReservation
        fields = "__all__"
        read_only_fields = ("id",)
