from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CreateSerializer, LoginSerializer


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    # 사용자 등록 뷰
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )  # 모든 사용자 허용
    serializer_class = CreateSerializer  # 사용자 생성 직렬화 클래스 사용


class LoginView(generics.CreateAPIView):
    # 사용자 로그인 뷰
    permission_classes = (permissions.AllowAny, )  # 모든 사용자 허용
    serializer_class = LoginSerializer  # 사용자 로그인 직렬화 클래스 사용

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(res, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # 클라이언트 토큰 삭제
        response = Response({"detail": "Logout Successful"}, status=status.HTTP_200_OK)
        response.delete_cookie('refresh')
        response.delete_cookie('access')
        return response


# RegisterView = RegisterView.as_view()
# LoginView = LoginView.as_view()
# LogoutView = LogoutView.as_view()
