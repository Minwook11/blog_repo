from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('case', CaseView.as_view()),
    path('search/size', views.SizeSearch),
    path('product/all', views.AllProduct),
    path('product/<int:product_id>', views.SelectRelatedPrac),
]
