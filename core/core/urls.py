"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home.views import *
from recipe.views import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'core'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('recipes/', Recipes_func, name='Recipe'),
    path('recipes/<id>', delete, name= 'delete recipe'),
    path('update-recipes/<id>', update, name="Update"),
    path('logout/', logout_page, name='logout'),
    path('admin/', admin.site.urls),
    path('students/', get_students, name='Students_name'),
    path('reportcard/', report_card, name=' reportcard')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT
                         )
