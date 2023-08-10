from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Message
from .serializers import ConversationSerializer, MessageSerializer

from decouple import config
import openai


openai.api_key = config('OPENAI_API_KEY')


class ChatbotView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "User must be authenticated."}, status=status.HTTP_403_FORBIDDEN)

        conversations_data = request.data.get('conversations', [])

        previous_conversations = []
        
        for conversation in conversations_data:
            role = conversation.get('role')
            prompt = conversation.get('prompt')
            
            # 이전 대화 기록 가져오기
            previous_conversations.append(f"{role}: {prompt}")

            previous_conversations_str = "\n".join(previous_conversations)

            prompt_with_previous = f"{previous_conversations_str}\n{role}: {prompt}\nAI:"

        model_engine = "text-davinci-003"
        completions = openai.Completion.create(
            # OpenAI 모델
            engine=model_engine,
            # 현재 사용자의 입력과 이전 대화 기록을 모두 포함
            prompt=prompt_with_previous,
            # 응답의 최대 길이
            max_tokens=2048,
            # 응답 개수
            n=5,
            # API가 추가 토큰 생성을 중지해야 하는 일련의 시퀀스를 지정하는 선택적 매개변수(지정하지 않을 경우 모델이 정지하기에 가장 좋은 위치를 결정)
            stop=None,
            # 응답의 무작위성 값이 낮을수록 출력에 집중하며, 높을수록 무작위 답변
            temperature=0.5,
        )
        response = completions.choices[0].text.strip()

        conversation_serializer = MessageSerializer(data={'user': user.id, 'role':role, 'prompt': prompt})

        if conversation_serializer.is_valid():
            conversation_serializer.save()
        else:
            return Response(conversation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 대화 기록에 새로운 응답 추가
        conversations_data.append({'role': 'AI', 'prompt': response})

        request.session['conversations'] = conversations_data
        request.session.modified = True
            
        return Response({'conversation': conversations_data})


class ConversationList(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 필요

    def get(self, request):
        messages = Message.objects.filter(user=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(Serializer.data)


class ConversationDetail(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 필요

    def get(self, request):
        try:
            message = Message.objects.filter(user=request.user).get(chatbot_id=chatbot_id)
        except Message.DoesNotExist:
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MessageSerializer(message)
        return Response(serializer.data)


class ConversationDelete(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 필요

    def get(self, request):
        try:
            message = Message.objects.filter(user=request.user).get(chatbot_id=chatbot_id)
        except Message.DoesNotExist:
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


ChatbotView = ChatbotView.as_view()
ConversationList = ConversationList.as_view()
ConversationDetail = ConversationDetail.as_view()
ConversationDelete = ConversationDelete.as_view()
