from django.urls import path, include
from . import views
from rest_framework import routers
from api.views import *

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'SaltyUsers', SaltyUserViewSet)

urlpatterns = [
    path('home/', views.APIView.as_view(), name='home'),
    path('list/', views.APIListView.as_view(), name='api_list'),
    path('saltylist/', views.SaltyUserListView.as_view(), name='salty_list'),
    path('saltyuser/', views.SaltyUserList.as_view()),
    path('saltyuser/<int:pk>/', views.SaltyUserDetail.as_view()),
]
