from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
        path('', views.index, name="index"),
        path('create', views.create, name="create"),
        path('read/<int:note_id>', views.read, name="read"),
        path('update/<int:note_id>', views.update, name="update"),
        path('delete/<int:note_id>', views.delete, name="delete"),
]
