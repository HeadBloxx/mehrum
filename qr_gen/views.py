from django.shortcuts import render
from django.http import HttpResponse
from administrative.models import Mehrum

# Create your views here.
def mehrum(request, id):
    mehrum_model = Mehrum.objects.get(id=int(id))
    return render(request, "qr_gen/mehrum.html", { "model": mehrum_model })