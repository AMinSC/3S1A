from rest_framework import serializers
from .models import Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = ['role', 'prompt']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['user', 'role', 'prompt']

