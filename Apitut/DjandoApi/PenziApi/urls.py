from django.conf.urls import url
from PenziApi import views


urlpatterns = [
    url(r"^UsersApi$", views.UsersApi),
    url(r"^UsersApi/([0-9]+)$", views.UsersApi),
    url(r"^MessagesApi$", views.MessagesApi),
    url(r"^MessagesApi/([0-9]+)$", views.MessagesApi),  # new
]
