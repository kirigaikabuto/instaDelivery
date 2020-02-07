from django.urls import path,include
from . import views

urlpatterns = [
    path('register_curier/',views.curier_register,name="register_curier"),
    path('private_сurier/',views.private_сurier,name="private_сurier"),
    path('private_curier/select/<int:id>',views.curier_select,name="curier_select"),
    path('private_curier/cancel/<int:id>',views.curier_cancel,name="curier_cancel"),
   
]
