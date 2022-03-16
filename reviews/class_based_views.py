from reviews.models import Review
from reviews.serializers import ReviewSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ReviewList(APIView):
    #Gets all reviews
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class ReviewDetail(APIView):
    def get(self, request, fk, format=None):
        reviews = Review.objects.filter(product = fk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
