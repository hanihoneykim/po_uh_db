from django.db import models
import uuid


class MyeongdongReservation(models.Model):
    BUILDING_CHOICES = [
        ("main_building", "본관"),
        ("new_building", "신관"),
        ("annex_building", "별관"),
    ]
    ROOM_TYPE_CHOICES = [
        ("family_suite", "패밀리스위트"),
        ("8_person_family_suite", "8인 패밀리 스위트"),
        ("cinema", "씨네마"),
        ("2_person_spa", "2인스파"),
        ("4_person_spa", "4인스파"),
        ("2_person_spa_suite", "2인스파 스위트"),
        ("4_person_spa_suite", "4인스파 스위트"),
        ("6_person_spa_suite", "6인스파 스위트"),
        ("6_person_spa_401", "6인스파 401"),
        ("6_person_spa_402", "6인스파 402"),
        ("8th_floor", "8층"),
    ]

    IS_CHECKED_IN_CHOICES = [
        ("checked_in", "투숙"),
        ("cancel", "취소"),
        ("before_check_in", "방문전"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    building_location = models.CharField(
        max_length=20, choices=BUILDING_CHOICES, blank=True, null=True
    )
    room_type = models.CharField(
        max_length=30, choices=ROOM_TYPE_CHOICES, blank=True, null=True
    )
    guest_name = models.CharField(max_length=40, null=True, blank=True)
    platform_name = models.CharField(max_length=30, null=True, blank=True)
    reservation_date = models.DateField(null=True, blank=True)
    lead_time = models.CharField(max_length=10, null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    length_of_stay = models.IntegerField(null=True, blank=True)
    total_room_charge = models.DecimalField(max_digits=10, decimal_places=0)
    adr = models.DecimalField(max_digits=10, decimal_places=0)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    guest_count = models.IntegerField(null=True, blank=True)
    relationship = models.CharField(max_length=10, null=True, blank=True)
    is_checked_in = models.CharField(
        max_length=30, choices=IS_CHECKED_IN_CHOICES, blank=True, null=True
    )
    is_minor = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
