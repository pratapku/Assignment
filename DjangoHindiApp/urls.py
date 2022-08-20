"""mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from .views import RegisterAPI
from django.contrib import admin
from django.urls import path 
from .views import Destroyeapi, Retriveapi, UserDetailAPI,RegisterUserAPIView, getapi, postapi
from rest_framework_simplejwt import views as jwt_views
from .import views
urlpatterns = [
    path("demoPage",views.demoPage),
    path("demoPage2",views.demoPage2),
    path('',views.loginUser,name="login"),
    path('signup',views.signupUser,name="signup"),
    path('signup_process',views.signup_process,name="signup_process"),
    path('login_proces',views.login_proces,name="login_proces"),
    path('home',views.home,name="home"),
    path('logout',views.logoutUser,name="logout"),
    path('add_tasks',views.add_tasks,name="add_tasks"),
    path('delete/<str:id>',views.delete_task,name="delete_task"),
    path('edit_task/<str:id>',views.edit_task,name="edit_task"),
    path('edit_tasks_save/<str:id>',views.edit_tasks_save,name="edit_tasks_save"),
    
    path('api/get/',getapi.as_view(), name='token_obtain_pair'),
    path('api/post/',postapi.as_view(), name='token_obtain_pair'),
    path('api/retrive/<int:pk>',Retriveapi.as_view(), name='token_obtain_pair'),
    path('api/destroye/<int:pk>',Destroyeapi.as_view(), name='token_obtain_pair'),
    
    path('api/register/',RegisterUserAPIView.as_view()),
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),



]
