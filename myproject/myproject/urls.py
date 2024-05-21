"""
URL configuration for myproject project.

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
from django.urls import path, include
import myapp.views as myapp_views
from myproject import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', myapp_views.PersonList.as_view()),
    path('person/create/', myapp_views.PersonCreate.as_view()),
    path('person/<int:pk>/', myapp_views.PersonDetail.as_view()),
    # auth
    path('auth/', include('myauth.urls', namespace='myauth')),
    path('logout/', LogoutView.as_view()),

    path('send/', myapp_views.send_mail),
    path('news/', myapp_views.NewsList.as_view()),
    path('news/create/', myapp_views.NewsCreate.as_view()),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls"))
    )
