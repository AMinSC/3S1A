from django.db import models
from django.contrib.auth import get_user_model
from chatbot.models import Message


User = get_user_model()

class Post(models.Model):
    CATEGORY_LIST = (
        ('새벽에 듣기 좋은', '새벽에 듣기 좋은'),
        ('드라이브 할 때 듣기 좋은', '드라이브 할 때 듣기 좋은'),
        ('운동할 때', '운동할 때'),
        ('집중할 때', '집중할 때'),
    )

    writer = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_LIST, null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True)
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
