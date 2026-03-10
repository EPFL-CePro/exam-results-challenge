from django.urls import path
from .views import passed_results

urlpatterns = [
    path("results/passed/", passed_results, name="passed_results"),
]
