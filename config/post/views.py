from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer

# # Create your views here.
# class ConversationToPostWrite(APIView):
#     def post(self, request, conversation_id):
#         conversation = get_object_or_404(Conversation, id=conversation_id)
#         title = request.data.get('title')
#         post = conversation.create_post(title)
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)