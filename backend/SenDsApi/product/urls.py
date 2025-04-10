

from django.urls import path
from .views import api_view, detailProductView, createProductView, updateProductView, deleteProductView, listProductView

urlpatterns=[
    path("", api_view, name="api_view"),
    path("<int:pk>/", detailProductView.as_view()),
    path("create/", createProductView.as_view()),
    path("<int:pk>/update/", updateProductView.as_view()),
    path("<int:pk>/delete/", deleteProductView.as_view()),
    path("list/", listProductView.as_view())
]