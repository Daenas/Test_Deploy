from django.shortcuts import render, HttpResponse, redirect
from .models import item
from .forms import CreateNewItem

def index(request):
    if request.method=="GET":
        form = CreateNewItem()
        return render(request, "index.html", {
            "item" : item.objects.all(),
            "form" : form,
            })
    elif request.method=="POST":
        content = request.POST.get('content')
        item.objects.create(content = content)
        form = CreateNewItem()
        return redirect("index")
    
def delete_item(request, item_id):
    item_toBeDeleted = item.objects.get(id = item_id)
    item_toBeDeleted.delete()
    return redirect("index")