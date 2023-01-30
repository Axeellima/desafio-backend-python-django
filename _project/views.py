from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import render

from store.models import Store

from store.views import StoreView

import requests

def home_page(request):
    return render(request, "docs_form.html")

def list_page(request):
    data = {}
    data["db"] = requests.get("http://localhost:8000/api/store/").json
    return render(request, "list_store.html", data)