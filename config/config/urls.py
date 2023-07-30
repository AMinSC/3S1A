from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', ),
    path('user/', include('user.urls')),
    path('chatbot/', include('chatbot.urls')),
    # path('post/', include('post.urls')),
]
