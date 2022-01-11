from django.shortcuts import render

# Create your views here.
def index(request):

    class Contact:
        id: int
        first_name: str
        last_name: str
        email: str
    
    contact1 = Contact()
    contact1.id=1
    contact1.first_name='Clayton' 
    contact1.last_name='Cook'
    contact1.email='ccook@example.com'

    context = {}
    # context = {"contact": contact1}
    request.contact = contact1

    return render(request, "core/index.html", context)

def contact_edit(request, contact):

    breakpoint()
    
    context = {"id": id,}
    return render(request, "core/contact_1_edit.html", context)

def contact_1_edit(request, id):

    breakpoint()
    
    context = {"id": id,}
    return render(request, "core/contact_1_edit.html", context)

def contact_1(request, id):

    context = {"id": id,}
    return render(request, "core/contact_1.html", context)