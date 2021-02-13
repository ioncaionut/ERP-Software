from django.shortcuts import render
# from django.http import HttpResponse
from .models import AisErp
# from django.contrib.auth.models import User
#  Create your views here.


def home(request):
    ais_erp_objects = AisErp.objects.all()
    context = {
            'ais_erp_objects': ais_erp_objects
    }
    return render(request,'AIS_ERP/home.html', context)





# def ais_erp_list_view(request):
#     ais_erp_objects = Ais.objects.all()
#     context = {
#         'ais_erp_objects': ais_erp_objects
#     }
#     return render(request, "AIS_ERP/home.html", context)

