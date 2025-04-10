

from rest_framework import status
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from rest_framework import generics

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
@api_view(['POST'])
def api_view(request):

    #if request.method != 'POST':
        #return Response({'detail': 'method get not allowed'}, status=405)
    # Ce request est une instance de la classe HTTP
    #query = Product.objects.all().order_by("?").first()  # Renvoie les données de façon aléatoire
    serializer = ProductSerializer (data = request.data)
    if   serializer.is_valid(raise_exception=True):
        #ici je save les données dans notre database
        serializer.save()
        return Response (serializer.data)
    else:
        return Response ({"detail": "invalide data"})
"""


## Databricks et airflow