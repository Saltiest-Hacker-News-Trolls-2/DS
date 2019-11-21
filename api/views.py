from django.shortcuts import render
from api.serializer import SaltyUserSerializer
from api.models import Items, SaltyUser
from django.views.generic import TemplateView, ListView
from rest_framework import serializers, viewsets
from rest_framework import generics
# Create your views here.

class APIView(TemplateView):
    template_name = "home.html"

class APIListView(ListView):
    model = Items
class SaltyUserListView(ListView):
    model = SaltyUser

class SaltyUserList(generics.ListCreateAPIView):
    queryset = SaltyUser.objects.all()
    serializer_class = SaltyUserSerializer

class SaltyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaltyUser.objects.all()
    serializer_class = SaltyUserSerializer