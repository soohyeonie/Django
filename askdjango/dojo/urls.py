from django.urls import include, path
from . import views

urlpatterns = [
    path('sum/<x>/', views.mysum),
    path('sum/<x>/<y>/', views.mysum),
    path('sum/<x>/<y>/<z>/', views.mysum),
]