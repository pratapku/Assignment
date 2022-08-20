"""DjangoHindiTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,include
from DjangoHindiApp import views
from django.conf.urls.static import static
from DjangoHindiTutorial import settings
# from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken import views
# from .import views

urlpatterns = [
    path('api/authlogin/', views.obtain_auth_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    # path("demoPage",views.demoPage),
    path("",include('DjangoHindiApp.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
