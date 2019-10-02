from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class CustomUser(AbstractUser):
    partner_link = models.CharField(max_length=30, verbose_name='партнерская ссылка', default='')
    invited_by = models.ForeignKey(
        'CustomUser',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    has_purchases = models.BooleanField(default=random.choice([True, False]))
    paid_for_partner = models.BooleanField(default=random.choice([True, False]))

    def __str__(self):
        return self.email
