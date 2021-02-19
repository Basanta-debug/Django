from django.shortcuts import render
from .models import Product
def index(request):
    return render(request,'products/index.html')

def new_html(request):
    products=Product.objects.all()
    context={
        'items':products
    }
    return render(request,'products/new_html.html',context)


