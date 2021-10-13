from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('case', CaseView.as_view()),
    path('search/size', views.SizeSearch),
    path('product/all', views.AllProduct),
    path('product/SR/<int:product_id>', views.SelectRelatedPrac),
    path('size/all', views.AllSize),
    path('size/FR', views.SizePrefetchRelatedPrac),
    path('complex/querystring', views.QueryStringPrac),
]
