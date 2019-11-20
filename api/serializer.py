from rest_framework import serializers
from api.models import SaltyUser

class SaltyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltyUser
        fields = [
            'id', 
            'hacker', 
            'hacker_salt_ranking', 
            'hacker_salt_ranking',
            'comment',
            'comment_saltiness_score',
        ]
