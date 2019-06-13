from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . forms import RegistrationForm
def index(request):

    form = RegistrationForm()
    context={
        "myregistrationform": form,
    }
    return render(request, "myfirstapp/index.html", context)
