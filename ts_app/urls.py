from django.urls import path
from . import views

urlpatterns = [
    path('trendsniper/', views.ts_backend, name='ts_backend'),
]