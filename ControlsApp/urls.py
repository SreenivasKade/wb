from django.urls import path
from . import views

app_name = 'ControlsApp'

urlpatterns = [
    path('', views.ControlView, name = 'control'),

    path('up/', views.UpView, name = 'up'),
    path('down/', views.DownView, name = 'down'),
    path('left/', views.LeftView, name = 'left'),
    path('right/', views.RightView, name = 'right'),
    path('stop/', views.StopView, name = 'stop'),
    path('api', views.APIControlView, name = 'control-api'),

]