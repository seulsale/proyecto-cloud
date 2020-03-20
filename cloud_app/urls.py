from django.urls import path
from . import views
from django.contrib.auth import logout
from .decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout, {'REDIRECT_URL': '/login'}, name='logout'),
    path('auth/', login_required(views.user_index), name='user_index'),
]
