from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='accounts'
urlpatterns=[
    path('',views.home,name="home"),
    path('register/',views.register,name="create_user"),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout')
]