from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('function/', views.PracticeView),
	path('nested/', views.NestedView),
]
