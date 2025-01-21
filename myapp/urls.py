
# from django.contrib import admin
from django.urls import path, include
from . import views

User_patterns = [
    path("", views.Users_list, name='Users_list'),
    path("add/", views.User_Add, name='User_Add'),
    path("view/<int:id>/", views.User_View, name='User_View'),
    path("copy/<int:id>/", views.User_Copy, name='User_Copy'),
    path("edit/<int:id>/", views.User_Edit, name='User_Edit'),
    path("destroy/<int:id>/", views.User_Destroy, name='User_Destroy'),
]

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    
    path("user/", include(User_patterns)),
]
