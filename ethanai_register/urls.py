from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.financial_form),
    path("<int:id>", views.financial_form, name = "update"),
    path("delete/<int:id>", views.financial_delete, name = "delete"),
    path("list/", views.financial_list)
    
]