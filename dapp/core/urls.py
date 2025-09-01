from django.urls import path
from .views import HomeView

app_name = "core"

urlpatterns = [
    path('json/', HomeView.as_view(), name='home'),
    
]

