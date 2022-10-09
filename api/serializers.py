from .models import Advocates, Company, Links
from rest_framework import serializers


class CompanyPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    summary = serializers.CharField(read_only=True)
    logo = serializers.ImageField(read_only=True)


class LinksPublicSerializer(serializers.Serializer):
    youtube = serializers.CharField(read_only=True)
    twitter = serializers.CharField(read_only=True)
    github = serializers.CharField(read_only=True)


class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanyPublicSerializer(read_only=True)
    links = LinksPublicSerializer(read_only=True)
    href = serializers.HyperlinkedIdentityField(
        view_name='adv_details',
        lookup_field='pk',
        read_only=True)

    class Meta:
        fields = ('id', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'href', 'company', 'links')
        model = Advocates

    # def create(self, validated_data):
    #     links = validated_data.pop('links')
    #     links_instance, created = Links.objects.create(name=links)
    #     advocates_instance = Advocates.objects.create(**validated_data, links=links_instance)
    #     return advocates_instance


class CompanySerializer(serializers.ModelSerializer):
    advocates = serializers.StringRelatedField(source='advocates_set', many=True)

    class Meta:
        fields = 'id', 'name', 'logo', 'summary', 'advocates'
        model = Company


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'youtube', 'github', 'twitter'
        model = Links
