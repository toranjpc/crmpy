
# from django.contrib import admin
from django.urls import path, include
from . import views

Users_patterns = [
    path("", views.Users_list, name='Users_list'),
    path("<int:id>/", views.Users_View, name='Users_View'),
    path("copy/<int:id>/", views.Users_Copy, name='Users_Copy'),
    path("edit/<int:id>/", views.Users_Edit, name='Users_Edit'),
    path("destroy/<int:id>/", views.Users_Destroy, name='Users_Destroy'),
]

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    
    path("users/", include(Users_patterns)),
]
