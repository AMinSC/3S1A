from django.urls import path
from .views import ChatbotView, ConversationList, ConversationDetail, ConversationDelete


app_name = 'chatbot'

urlpatterns = [
    # Chatbot과 대화
    path('', ChatbotView),
    # 대화 내용 리스트
    path('conversations/', ConversationList, name='list'),
    # 저장된 리스트 중 상세 페이지
    path('conversations/<int:chatbot_id>/', ConversationDetail, name='detail'),
    # 대화내용 삭제
    path('conversations/<int:chatbot_id>/delete/', ConversationDelete, name='delete'),
]
