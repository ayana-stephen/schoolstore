from django.urls import path
from .import views
app_name='store'
urlpatterns = [

    path('', views.index,name='index'),
    path('home', views.order, name="order"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('newform', views.newform, name="newform"),

    path('load_course',views.load_course, name='load_course'),



]