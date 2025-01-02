from django.urls import path
from . import views

urlpatterns = [
    path('api/get-details/', views.get_input, name='get_input'),

]
