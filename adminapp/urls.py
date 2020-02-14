
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.index,name="curiers"),
    path("curiers/balance_add_form/<int:id>/",views.balance_add_form,name="balance_add_form"),
    path("curiers/balance_add_form_action/",views.balance_add_form_action,name="balance_add_form_action")
]
