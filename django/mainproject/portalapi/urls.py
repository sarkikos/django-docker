from django.urls import path
from  . import views

urlpatterns = [
  path('version/', views.get_version)
]