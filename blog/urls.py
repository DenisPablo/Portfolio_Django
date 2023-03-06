from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_post, name="posts"),
    path("<int:post_id>", views.detalles_post),
]
