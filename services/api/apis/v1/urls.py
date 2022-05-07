from django.urls import path, include

urlpatterns = [path('users/', include('apis.v1.users.urls'))]
