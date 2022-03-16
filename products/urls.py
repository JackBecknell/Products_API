from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import function_based_views
from . import class_based_views

urlpatterns = [
    path('', class_based_views.ProductList.as_view()),
    path('<int:pk>/', class_based_views.ProductDetail.as_view())
]
