from rest_framework import serializers
from .models import Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'title', 'user', 'prompt', 'response', 'timestamp']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'title', 'content', 'user']


class ConversationSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=200)
    prompt = serializers.CharField()
