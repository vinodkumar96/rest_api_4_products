from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super (JSONResponse,self).__init__(content,**kwargs)
def input(request):
    return render(request,'input.html')
def link(request):
    p_id1 = int(request.POST['t1'])
    p_name1 = request.POST['t2']
    p_cost1 = float(request.POST['t3'])
    p_mfd1 = request.POST['t4']
    p_exd1 = request.POST['t5']
    f =Product(p_id=p_id1,p_name=p_name1,p_cost=p_cost1,p_mfd=p_mfd1,p_exd=p_exd1)
    f.save()
    return render(request,'link.html')
def display(request):
    recs = Product.objects.all()
    return render(request,'display.html',{'recs':recs})
def productapi(request):
    data = Product.objects.all()
    serial = ProductSerializer(data,many=True)
    return JSONResponse (serial.data)