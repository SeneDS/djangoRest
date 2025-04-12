

from django.urls import path
from .views import api_view, ProductsMixinView , ListCreateAPIView #detailProductView, createProductView, updateProductView, deleteProductView, listProductView







urlpatterns=[
    #path("", api_view, name="api_view"),
    #path("<int:pk>/", detailProductView.as_view()),
    #path("create/", createProductView.as_view()),
    #path("<int:pk>/update/", updateProductView.as_view()),
    #path("<int:pk>/delete/", deleteProductView.as_view()),
    #path("list/", listProductView.as_view()),
    #path("mixins/", ProductsMixinView.as_view()),

    # URL pour créer un produit
    path("create-list/", ListCreateAPIView.as_view(), name="product-create"),

    # URL pour obtenir un produit par son ID
    path("<int:pk>/detail/", ProductsMixinView.as_view(), name="product-detail"),

    # URL pour mettre à jour un produit
    path("<int:pk>/update/", ProductsMixinView.as_view(), name="product-update"),

    # URL pour supprimer un produit
    path("<int:pk>/delete/", ProductsMixinView.as_view(), name="product-delete"),

    # URL pour lister les produits
    path("list/", ProductsMixinView.as_view(), name="product-list"),

    # URL pour les mixins (je pourais vouloir spécifier ce nom pour des tests ou des actions supplémentaires)
    path("mixins/", ProductsMixinView.as_view(), name="product-mixins"),
    ]
