from django.urls import path
from . import views
urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("healthbot/", views.healthbot_page, name="healthbot"),
]

