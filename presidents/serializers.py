# members/serializers.py
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from .models import President




class PresidentListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='president-api:detail')
    total_ranking = serializers.SerializerMethodField()
    short_details = serializers.SerializerMethodField()

    class Meta:
        model = President
        fields = ['name', 'image', 'short_details', 'health_rating', 'education_rating', 'security_rating', 'infrastructure_rating', 'total_ranking', 'url']

    def get_total_ranking(self, obj):
        return obj.calculate_total_ranking()
    
    def get_short_details(self, obj):
        # Return the first 50 characters of the details field
        return obj.details[:50] + ".." if obj.details else None

class PresidentSerializer(ModelSerializer):
    total_ranking = serializers.SerializerMethodField()

    class Meta:
        model = President
        fields = ['name', 'image', 'details', 'health_rating', 'education_rating', 'security_rating', 'infrastructure_rating', 'total_ranking']
    
    def get_total_ranking(self, obj):
        return obj.calculate_total_ranking()
    

    
