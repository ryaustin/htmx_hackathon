from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}
    return render(request, "core/index.html", context)

def contact_1_edit(request, id):
    
    context = {"id": id,}
    return render(request, "core/contact_1_edit.html", context)

def contact_1(request, id):

    context = {"id": id,}
    return render(request, "core/contact_1.html", context)