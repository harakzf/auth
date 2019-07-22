from django.urls import path
from .views import SampleView

app_name = 'sampleapp'

urlpatterns = [
    path('', SampleView.as_view(), name='sample_view'),
]

