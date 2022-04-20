from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home_index.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('homes/', views.HomeList.as_view(), name="homelist"),
    path('homes/create', views.Home_Create.as_view(), name="home_create"),
    path('homes/<int:pk>/', views.Home_Detail.as_view(), name="home_detail"),
    path('homes/<int:pk>/update', views.Home_Update.as_view(), name="home_update"),
    path('homes/<int:pk>/delete', views.Home_Delete.as_view(), name="home_delete"),
    path('user/<username>/', views.profile, name='profile'),  
#Car Route
    path('cars/', views.car_home, name='car_index'),
    path('cars/<int:car_id>', views.car_show, name='car_show'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create'),
]


