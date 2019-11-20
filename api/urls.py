from django.urls import path, include
from . import views
from rest_framework import routers
from api.views import APIListView, APIView, SaltyUserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'SaltyUsers', SaltyUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.APIView.as_view(), name='home'),
    path('list/', views.APIListView.as_view(), name='api_list'),
    
]
