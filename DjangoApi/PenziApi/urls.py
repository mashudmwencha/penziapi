from django.urls import path
from . import views

urlpatterns = [
    path("message-receive/", views.message_receive_view, name="message_receive_view"),
    path("user-profiles/", views.get_user_profile, name="user-profiles"),
    path("user-details/", views.get_user_details, name="user-details"),
    path(
        "merged-user-data/<int:user_id>/",
        views.merge_user_data,
        name="merged-user-data",
    ),
]
