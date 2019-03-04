# restApi/urls.py
from django.conf.urls import url
from django.urls import include, path
from rest_auth.views import UserDetailsView

from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('users', views.UserListView.as_view()),
    url(r'user/',UserDetailsView.as_view())
]
