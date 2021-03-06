"""wt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,reverse,re_path
from django.conf.urls import handler404,handler500
from django.conf import settings

from .import views

handler404='wt.views.handler404'
handler500='wt.views.handler500'

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('article1/',views.contact,name='article1'),
    path('news/',views.contact,name='News'),

    path('blog/', include('blog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members',include('members.urls')),
    path('admin/', admin.site.urls),
    path('Shop/',include('shop.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
