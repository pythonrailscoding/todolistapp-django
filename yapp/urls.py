from django.urls import path
from . import views
from .views import UserList, UserCreateView, UserUpdateView, UserDetailView, UserDeleteView

urlpatterns = [
    path('', UserList.as_view(), name='index'),
    path('create', UserCreateView.as_view(), name='create'),
    path('update\<int:pk>', UserUpdateView.as_view(), name='update'),
    path('detail\<int:pk>', UserDetailView.as_view(), name='detail'),
    path('delete\<int:pk>', UserDeleteView.as_view(), name='delete'),
]
