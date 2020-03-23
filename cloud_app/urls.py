from django.urls import path
from . import views
from .decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('auth/', login_required(views.TODOList.as_view()), name='user_index'),
    path('auth/add/', login_required(views.TODOCreate.as_view()), name='user_add'),
    path('auth/<int:pk>/', login_required(views.TODOUpdate.as_view()), name='user_update'),
    path('auth/<int:pk>/delete', login_required(views.TODODelete.as_view()), name='user_delete'),
]
