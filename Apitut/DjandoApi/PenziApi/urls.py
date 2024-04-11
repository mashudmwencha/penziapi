from django.conf.urls import url
from PenziApi import views


urlpatterns = [
    url(r"^PenziApi$", views.PenziApi),
    url(r"^PenziApi/([0-9]+)$", views.PenziApi),
    url(r"^MessagesApi$", views.MessagesApi),
    url(r"^MessagesApi/([0-9]+)$", views.MessagesApi),  # new
]
