from rest_framework import serializers
from .models import Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=200)
    prompt = serializers.CharField()
    
    class Meta:
        model = Conversation


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'title', 'content', 'user']

