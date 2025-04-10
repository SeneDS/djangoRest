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






















#Sources:
https://medium.com/p/1d2de182954b
https://medium.com/p/1d2de182954b