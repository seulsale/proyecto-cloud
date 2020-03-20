from django.urls import path
from . import views
from .decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('auth/', login_required(views.user_index), name='user_index'),
]
