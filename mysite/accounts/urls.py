from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views as accounts_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^signup/$', accounts_views.signup, name='signup'),
url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
