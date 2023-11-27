from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("append_tag/<int:pk>", views.append_tag, name="append-tag"),
    path("form_search", views.form_search, name="form-search")
]
