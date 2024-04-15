from django.db import models
import uuid


class Guest(models.Model):
    GUEST_TYPE_CHOICES = [
        ("individual", "개인"),
        ("corporate", "법인"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    guest_name = models.CharField(max_length=40, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    guest_type = models.CharField(
        max_length=30, choices=GUEST_TYPE_CHOICES, blank=True, null=True
    )
    credit_card_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    visit_count = models.IntegerField(null=True, blank=True)
