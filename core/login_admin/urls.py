from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_admin , name="login"),
    path('register/', views.register , name="register"),
    path('logout/' , views.logout_user , name = 'logout')
]