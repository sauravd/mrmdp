from django.urls import path
from .views import HomePageView, AccessToRoadnetworkView, AgriLivstkCooperativesView, AnimalHusbandryFirmsView


urlpatterns = [
    path("", HomePageView.as_view(), name="index"), 
    path("accesstoroadnetwork/",AccessToRoadnetworkView, name="accesstoroadnetwork"),
    path("agrilivstkcooperative/",AgriLivstkCooperativesView, name="agrilivstkcooperative"),
    path("animalhusbandryfirms/",AnimalHusbandryFirmsView, name="animalhusbandryfirms"),
]
