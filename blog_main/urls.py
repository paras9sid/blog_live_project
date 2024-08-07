"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blog_app import views as BlogsView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #home + posts rendered views
    path('',views.home,name='home'),
    
    #category path
    path('category/',include('blog_app.urls')),

    path('<slug:slug>/',BlogsView.blogs,name='blogs'),
    # Search endpoint
    path('blogs/search/',BlogsView.search,name='search'),
    path('register/',BlogsView.register,name='register'),
    path('login/',BlogsView.login,name='login'),
    path('logout/',BlogsView.logout,name='logout'),

    path('dashboard/',include('dashboards.urls')),
    path('pass/',include('pass_res.urls')),


    path('dashboard',include('dashboards.urls')),


] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
