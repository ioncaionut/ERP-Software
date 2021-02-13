from django.shortcuts import render
from django.http import HttpResponse
from .models import AIS_ERP
# Create your views here.

def ais_erp_list_view(request):
    ais_erp_objects = AIS_ERP.objects.all()
    context = {
        'ais_erp_objects': ais_erp_objects
    }
    return render(request, "ais_erp/index.html", context)

