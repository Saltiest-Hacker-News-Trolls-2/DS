from rest_framework import serializers
from api.models import SaltyUser

class SaltyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltyUser
        fields = ['by', 'salty_score', 'sarcasm_core', 'catagory']
