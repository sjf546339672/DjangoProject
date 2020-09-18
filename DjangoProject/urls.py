"""DjangoProject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from DjangoProject.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include("student.urls")),
    path('movie/', include("movie.urls")),
    path('stuone/', include("stuone.urls")),
    path('stutwo/', include("stutwo.urls")),
    path('stufive/', include("stufive.urls")),
    path('stusix/', include("stusix.urls")),
    path('stuseven/', include("stuseven.urls")),
    path('stueight/', include("stueight.urls")),
    path('stunine/', include("stunine.urls")),
    path('stuten/', include("stuten.urls")),
    path('stueleven/', include("stueleven.urls")),
    path('stutwelve/', include("stutwelve.urls")),
    path('api/v1/', include("rest001.urls")),
    path('api/', include("rest002.urls")),
]

from django.views.static import serve
if DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}))
