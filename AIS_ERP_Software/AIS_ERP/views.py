from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse(" You're at the AIS_ERP main.")

