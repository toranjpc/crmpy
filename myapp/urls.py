# from django.contrib import admin
from django.urls import path, include
from . import views
from . import user_auth_views

User_patterns = [
    path("KindList/", views.User_Category_list, name='User_Kind_list'),
    path("KindList/add/", views.User_Category_Add, name='User_Kind_Add'),
    path("KindList/view/<id>/", views.User_Category_Edit, name='User_Kind_View'),
    path("KindList/edit/<int:id>/", views.User_Category_Edit, name='User_Kind_Edit'),
    path("KindList/destroy/<int:id>/", views.User_Category_Destroy, name='User_Kind_Destroy'),

    path("GroupList/", views.User_Group_list, name='User_Group_list'),
    path("GroupList/add/", views.User_Group_Add, name='User_Group_Add'),
    path("GroupList/view/<id>/", views.User_Group_Edit, name='User_Group_View'),
    path("GroupList/edit/<int:id>/", views.User_Group_Edit, name='User_Group_Edit'),
    path("GroupList/destroy/<int:id>/", views.User_Group_Destroy, name='User_Group_Destroy'),

    
    path("", views.Users_list, name='Users_list'),
    path("add/", views.User_Add, name='User_Add'),
    path("view/<id>/", views.User_View, name='User_View'),
    path("copy/<int:id>/", views.User_Copy, name='User_Copy'),
    path("edit/<int:id>/", views.User_Edit, name='User_Edit'),
    path("destroy/<int:id>/", views.User_Destroy, name='User_Destroy'),

]

urlpatterns = [
    path('login/', user_auth_views.login_view, name='login'),
    path('logout/', user_auth_views.logout_view, name='logout'),
    path('signup/', user_auth_views.register_view, name='signup'),

    path("", views.dashboard, name='dashboard'),
    
    path("user/", include(User_patterns)),
]

