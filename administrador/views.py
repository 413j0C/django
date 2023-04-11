from django.shortcuts import render

# Create your views here.

def activosTotales(request):
    return render(request,'dashboard/panelAdministracion.html')

def formatoPdf(request):
    return render(request,'dashboard/registroPDF.html')




