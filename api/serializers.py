from .models import Advocates, Company
from rest_framework import serializers


class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'company', 'links')
        model = Advocates


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'name', 'profile_pic', 'summary'
        model = Company
