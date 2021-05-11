from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("rahat", views.rahat, name="rahat"),
    # path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet") #any string with string variable "name"
]