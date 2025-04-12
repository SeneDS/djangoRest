

from rest_framework import status
from rest_framework.views import APIView

from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from rest_framework import generics, mixins,  authentication, permissions
from rest_framework.authentication import TokenAuthentication
from .permissions import  IsStaffPermission



class ListCreateAPIView (generics.ListCreateAPIView ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]
    #Là on remplit le champ content par le nom du produit si content n'est pas renseigné
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = name
        serializer.save(content=content)

# Toutes ces classes peuvent etre mises dans une seule classe avec du mixins
""""
class detailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class createProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #Là on remplit le champ content par le nom du produit si content n'est pas renseigné
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = name
        serializer.save(content=content)


class updateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = name
        serializer.save(content=content)

class deleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Produit supprimé avec succès ✅"}, status=status.HTTP_204_NO_CONTENT)


#Les listes afficher tous les produits qui sont au niveau backend
class listProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

"""

class ProductsMixinView(
        generics.GenericAPIView,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,  # Ajout pour la liste des produits
        mixins.RetrieveModelMixin,  # Pour les détails
        mixins.DestroyModelMixin):  # Pour la suppression


    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #Là on remplit le champ content par le nom du produit si content n'est pas renseigné
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = name
        serializer.save(content=content)


    # Personnalisation de la mise à jour (utilise perform_update)
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)


    # Définir la méthode GET pour la liste ou les détails
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)  # Détail du produit
        return self.list(request, *args, **kwargs)  # Liste des produits


    # Méthode POST pour la création d'un produit
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # Méthode PUT pour la mise à jour d'un produit
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Méthode PATCH pour la mise à jour partielle d'un produit
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

        # La méthode destroy() est déjà incluse grâce à DestroyModelMixin
        # Il suffit d'appeler `destroy()` en cas de requête DELETE.

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)







