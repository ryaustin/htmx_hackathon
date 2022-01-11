from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}
    return render(request, "core/index.html", context)

def contact_1_edit(request):

    context = {}
    return render(request, "core/contact_1_edit.html", context)