from django.urls import path

from . import views
from mapview.views import MapView

urlpatterns = [
    path("", MapView.as_view(), name='map'),
]
