from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^HandleSms$", views.HandleSms, name="HandleSms"),
]
