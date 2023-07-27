from django.urls import path
from .views import ChatbotView


app_name = 'chatbot'

urlpatterns = [
    # chatbot과 대화
    path('conversation/', ChatbotView.as_view()),
    # ChatbotView 클래스가 대화 내용을 자동 저장
    # 대화 내용이 저장된 리스트
    # path('', ),
    # # 저장된 리스트 중 상세 페이지
    # path('<int:chatbot_id>/', ),
    # # 대화내용 삭제
    # path('<int:chatbot_id>/delete/', ),
]
