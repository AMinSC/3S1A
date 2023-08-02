from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, blank=True)
    prompt = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self. prompt}: {self. response}"
    
    def create_post(self, title=None):
        if not title:
            title = self.timestamp.strftime('%Y-%m-%d %H:%M')
        post = Message(conversation=self, user=self.user, role=self.role, prompt=self.prompt)  # title=title, content=self.response, author=self.user)
        post.save()
        return post


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, blank=True)
    prompt = models.TextField(blank=True)
