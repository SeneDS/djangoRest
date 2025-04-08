from tkinter.font import names

from django.http import JsonResponse
from django.template.defaultfilters import first
from .models import Product
from django.forms.models import model_to_dict


# Create your views here.
def api_view(request):
 # ce request est different de ce requests. Le premier c'est une instance de la classe httP et l'autre c'est une luvraurie qui nous permet de construire des clients.
    query = (Product.objects.all()).order_by("?").first() ##order_by("?") permet de renvoyer les données de façon aleatoire
    data = {}
    if query:
        data = model_to_dict(query)
     #ça c'est ce qu'on appelle la serialisation. Il s'agit de mettre des données sous forme de dictionnaire
    return JsonResponse(data)