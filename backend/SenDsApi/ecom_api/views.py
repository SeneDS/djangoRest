

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
import json



def api_view(request, *args, **kwargs):
    # request ==> HTTpRequests instance
    data = {"nom" : "eteinne"}
    return JsonResponse(data)


"""
def api_view(request, *args, **kwargs):
    # request ==> HTTpRequests instance
    print(request.body)
    data = json.loads(request.body)
    print(data)
    #data["headers"] = request.headers
    print(request.headers)
    data["params"] = dict(request.GET)
    data["post-data"] = dict(request.POST)
    data["content_type"] = request.content_type
    return JsonResponse(data)
"""