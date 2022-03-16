from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import class_based_views

urlpatterns = [
    path('', class_based_views.ReviewList.as_view()),
    #will add a future path here for when pk is passed as well
    path('<int:fk>/', class_based_views.ReviewDetail.as_view())
]