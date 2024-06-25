# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HomeView(generics.ListAPIView):
    authentication_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'AUTHENTICATED!'
        }
        return Response(response, status=200)
