from django.urls import path
from . import views

urlpatterns = [
    path('/', views.DataTruckView.as_view(), name='data'),
]