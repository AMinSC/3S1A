from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    MEMBER_STATUS = [
        ('GM', 'General Member'),
        ('AM', 'Associate Member'),
        ('RM', 'Regular Member'),
    ]

    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    member_status = models.CharField(
        max_length=2,
        choices=MEMBER_STATUS,
        default='GM',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def user_post_rating(self):
        num_posts = self.post_set.count()
        if num_posts >= 100:
            self.member_status = 'RM'
        elif num_posts >= 30:
            self.member_status = 'AM'
        else:
            self.member_status = 'GM'
        self.save()
        return self.member_status
