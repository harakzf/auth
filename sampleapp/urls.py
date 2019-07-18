from django.urls import path
from .views import LoginView

app_name = 'sampleapp'

urlpatterns = [
    path('', LoginView.as_view(), name='login_view'),
]

