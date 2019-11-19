from django.shortcuts import render
from api.serializer import SaltyUserSerializer
from api.models import Items, SaltyUser
from django.views.generic import TemplateView, ListView
from rest_framework import serializers, viewsets
# Create your views here.

class APIView(TemplateView):
    template_name = "api.html"

class APIListView(ListView):
    model = Items

class SaltyUserViewSet(viewsets.ModelViewSet):
    queryset = SaltyUser.objects.all()
    serializer_class = SaltyUserSerializer

# def saltiest_score:
#     calc_salyy = 'super salty'
#     calc_salty_user = 'salty user'
#     SaltyUser.objects.create(
#         score = calcty
#         user

#     )