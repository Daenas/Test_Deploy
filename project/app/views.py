from django.shortcuts import render, HttpResponse
from .models import item

def index(request):
    if request.method=="GET":
        return render(request, "index.html", {
            "item" : item.objects.all()
            })