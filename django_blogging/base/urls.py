from django.urls import path
from .views import *

urlpatterns = [
    path('case', CaseView.as_view()),
]
