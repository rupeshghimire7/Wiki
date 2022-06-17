from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.entry, name = 'entry'),
    path("search", views.search, name= 'search'),
    path("newpage",views.create,name='create'),
    path("random",views.random,name='random'),
    path("edit/<title>", views.edit, name='edit')
]
