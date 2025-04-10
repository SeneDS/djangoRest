

from rest_framework import status
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer





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
@api_view(['GET'])
def api_view(request):

    #if request.method != 'POST':
        #return Response({'detail': 'method get not allowed'}, status=405)
    # Ce request est une instance de la classe HTTP
    query = Product.objects.all().order_by("?").first()  # Renvoie les données de façon aléatoire
    data = {}
    if query:
        #data = model_to_dict(query, fields=["name", "price", "description"])
        # Sérialisation sous forme de dictionnaire
        data =ProductSerializer(query).data
    return Response(data)
    """


## Databricks et airflow