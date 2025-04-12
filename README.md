# **djangoRest**:
On cree deux dossiers
J'ai installé les librairies suiventes:
Django
django-cors-headers
djangorestframework
pyyaml
requests

On cree deux dossier backend et client_api. L'api est crée dans backend via la commande suivante: 
```shell
django-admin startproject SenDsApi
cd SenDsApi
django-admin startapp product
```
puis ajouter l'application product dans liste des applications qui sont dans le fichier settings. Créeons une nouvelle application nomée api qu'on ajoute dans les settings.
puis j'ai fait  
``shell 
python3 manage.py runserver 8081
``

root: http://127.0.0.1:8001/ecom_api/api_view/

On peut faire des api avec django mais django a ses limites.

basic.py
```python
endpoint = "http://127.0.0.1:8001/ecom_api/api_view/"
responses = requests.get(endpoint)
print(responses.json())
print(responses.status_code)
```

views.py
```python
def api_view(request, *args, **kwargs):
    data = {
        "name" :"etienne",
        "langage": "python",
    }
    return JsonResponse(data)
```

senDsApi/urls.py
```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecom_api/', include('ecom_api.urls')),
]


```

ecom_api/urls.py

```python
from django.urls import path
from .views import api_view

urlpatterns = [
    path('api_view/', api_view, name='api_view'),
```

NB: pour converir les données en dictionnaire c'est le loads exemple: `` data = json.loads(request.body)``. Et pour revenir au type de données initiales on fait un  dumps pax exemple:
``data = json.dumps(request.body)``

## 6. Comment renvoyer les données qui sont dans le database


on cree un modele dans product. 
puis on enregistre des produits:
``python3 manage.py shell
from product.models import Product
Product.objects.create(name='Orange', content='description here', price=3.99)
exit

``
## Récuperer les données de la base de données au format json
Nous allons dans product et nous avons effectué les dopérations suivantes:

### 1. Creation du model 
```python
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
```

### 2. Creation de la vue
```python 
from django.http import JsonResponse
from django.template.defaultfilters import first
from .models import Product
from django.forms.models import model_to_dict

def api_view(request):# Create your views here.
def api_view(request):
 # ce request est different de ce requests. Le premier c'est une instance de la classe httP et l'autre c'est une luvraurie qui nous permet de construire des clients.
    query = (Product.objects.all()).order_by("?").first() ##order_by("?") permet de renvoyer les données de façon aleatoire
    data = {}
    if query:
          data = model_to_dict(query, fields=[ "name", "price", "description"])#on peut ne pas spécifier ça: , fields=[ "name", "price", "description"]
     #ça c'est ce qu'on appelle la serialisation. Il s'agit de mettre des données sous forme de dictionnaire
    return JsonResponse(data)
```
### 4. Creation de l'urls
```python

from backend.SenDsApi.SenDsApi.urls import urlpatterns
from backend.SenDsApi.product.views import api_view

urlpatterns=[
    path("", api_view, name="api_view"),
]
```

Puis refferencer l'url dans le fichier urls principal du projet:SenDsApi/urls.py
```python
 path('product/', include('product.urls'))

```
##Les limite de django pour les api
si on fait un ctrl et on clique sur JsonResponse. On voit qu'il herite de httpresponse alors que ce dernier ne renvoie rien d'autre que du html. 

## Django REST Serializers et Model API Partie 8
on cree le fichier forms.py et le fichier serializer.py. Le serializer c'est comme le model en django


 jusqu'ici nous avons codé nos propres vues. Dans ce qui suit nous verrons comment utiliser les vues génériques. 


## Les vues génériques
cela permet de créer des vues avec du moindre code. En utilisant les classes base view un autre developpeur poura les comprendre facilement.

CRUD: create, retreave, update, delate

### On peut travailler sur les permissions maintenant afin que n'importe qui ne puisse faire n'importe quoi.
Il y'a plusieurs types d'authentaification. Il faut juste l'intoduire dquelques lignes de codes dans la classe consernée.

Imports
```python
from rest_framework import generics, mixins,  authentication, permissions
```
#### 1.1. authentification par session (django views permission)
Exemple de code 
```python
class ListCreateAPIView (generics.ListCreateAPIView ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly]
    #Là on remplit le champ content par le nom du produit si content n'est pas renseigné
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = name
        serializer.save(content=content)
```
on peut avoir aussi:
En plus de SessionAuthentication, il y'a BasicAuthentication, TokenAuthentication, 
Pour les permissions il y'a IsAdminUser, IsAuthenticatedOrReadOnly, RemoteUserAuthentication
#### 1.1. django model permission
on crerer un superuser avec 
python3 manage.py createsuperuser

puis on se connect à admin, on cree un secon utilisateur, on cree un groupe avec des permission, on l'ajoute au groupe et on lui donne des permissions spécifiques. On le fait également staff member.
Ces authorisations sont accès sur le modele et pas sur la vue. En effet, s'ajit de determiner qui peut voir les données d'un modele,qui peut en rajouter, en modifier ou en supprimer.
```python
#Code de remplacement dans la vue



class ListCreateAPIView (generics.ListCreateAPIView ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    #Là on remplit le champ content par le nom du produit si content n'est pas renseigné
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = name
        serializer.save(content=content)
```
Pour que les données s'enregistre dans la session admin il nous faut mettre ces lignes de codes dans admin.py
```python
from django.contrib import admin
from .models import Product
admin.site.register(Product)
```
 et rajouter celles-ci dans models.py pour afficher les noms des champs:
```python
    def __str__(self):
        return self.name
```
La limite de django modele permission c'est qu'on peut donner à une personne que la permission ce qui lui donne l'accès en lecture de toutes les données de la table en question. Tout le monde peut voir les produits par exemple.

#### Les permissions personnalisées, la surcharge du DjangoModelPermissions.
nb: avec DjangoModelPermissions, un utilisateur peut ne pas avoir acces à la lecture des données depuis admin mais il peut en avoir acces depuis le endpoint: http://127.0.0.1:8001/product/create-list/ par exemple.

Ains on va creer un fichier permission.py dans le dossier product.

####Token authentication
jusqu'ici nous avons utilisé la SessionAuthentication maintenant, nous utiliserons le tokenAuthentication. 













#Sources:
https://medium.com/p/1d2de182954b
https://medium.com/p/1d2de182954b