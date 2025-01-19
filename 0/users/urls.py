from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView
from . import views

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),


    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]