from django.urls import path
from .views import AdvDetail, AdvList, CompanyList, CompantDetail


urlpatterns = [
    path('advocates', AdvList.as_view()),
    path('advocates/<int:pk>/', AdvDetail.as_view()),

    path('companies', CompanyList.as_view()),
    path('companies/<int:pk>/', CompantDetail.as_view())
]
