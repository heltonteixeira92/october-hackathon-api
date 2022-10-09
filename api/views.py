from rest_framework import generics
from .models import Advocates, Company
from .serializers import AdvocateSerializer, CompanySerializer


class AdvList(generics.ListCreateAPIView):
    queryset = Advocates.objects.all()
    serializer_class = AdvocateSerializer


class AdvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advocates.objects.all()
    serializer_class = AdvocateSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
