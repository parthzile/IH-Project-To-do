from django.urls import path
from . import views

urlpatterns = [
	path('home', views.index, name="home"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('',views.loginPage, name= "login"),
    path('login/',views.loginPage, name= "login"),
    path('register/',views.registerPage, name= "register"),
    path('logout/',views.logoutUser, name= "logout")

]