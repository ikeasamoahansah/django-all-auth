# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

class HomeView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.'
        }
        return Response(response, status=200)