from django.urls import path
from . import views 

urlpatterns = [
    path("", views.main_view, name="staff_main_view"),
    path("<int:staff_id>/", views.staff_id_view, name="staff_id"),
    path("test/", views.test, name="test"),
]
