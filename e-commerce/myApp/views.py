from django.shortcuts import get_object_or_404, render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from . import models
from .models import Product
from decimal import Decimal
from django.db.models import Avg,Max,Min
from .form import formProduct,formFiles
from django.contrib.auth.decorators import login_required
import random,os


data={
    "telefon":["samsung s20","Samsung s11"],
    "bilgisayar":["laptop 1","laptop 2"],
    "elektronik":[]

}
def index(request):
    # list_items=""
    product=models.Product.objects.filter(isActivate=True).order_by("price")
    product_count=models.Product.objects.filter(isActivate=True).count()
    product_price=models.Product.objects.filter(isActivate=True).aggregate(Avg("price"),Max("price"),Min("price"))
    # category_list=list(data.keys())
    # for category in category_list:
    #     redirect_path=reverse("category_get",args=[category])
    #     list_items+=f"<li><a href=\"{redirect_path}\">{category}</a></li>"
    

    # html=f"<ul>{list_items}</ul>"
    # return  HttpResponse(html)
    return render(request,"myapp/index.html",{
        # "categories":category_list,
        "products":product,
        "now":datetime.now,
        "count":product_count,
        "price":product_price
    })

def details(request,slug):
    # try:
    #  product=models.Product.objects.get(pk=id)
    # except:
    #  raise Http404()
    product=get_object_or_404(models.Product,slug=slug)
    content={
        "product":product
    }
    return render(request,"myapp/details.html",content)

def list(request):
    if 'q' in request.GET and request.GET.get('q'):
        q=request.GET['q']
        product=models.Product.objects.filter(name__contains=q).order_by("-price")
        
    else:
        product=models.Product.objects.all().order_by("-price")
       

   
    content={
    "products":product
    }
     
    return render(request,"myapp/list.html",content)
@login_required(login_url="/account/login")
def create(request):
    
    if request.method == "POST":
        form=formProduct(request.POST,request.FILES)
        
        if form.is_valid():
         form.save()
         return redirect("list_view")
   
    else:
     form=formProduct()
    return render(request, "myapp/create.html", {"form":form})

def handle_uploaded_file(file):
    # Kaydedilecek dizini kontrol et ve oluştur
    temp_dir = "temp/"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)  # Dizin yoksa oluştur

    # Dosya adını oluştur
    number = random.randint(1000, 9999)
    filename, file_extension = os.path.splitext(file.name)
    name = filename + "_" + str(number) + file_extension

    # Dosyayı kaydet
    file_path = os.path.join(temp_dir, name)  # Tam yol oluştur
    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    print(f"Dosya kaydedildi: {file_path}")

def uploud(request):
   if request.method=='POST':
      form=formFiles(request.POST,request.FILES)
      
      if form.is_valid():
        model=models.FileUploudModel(image=request.FILES['image'])
        model.save()
      return render(request,'myapp/success.html')
   else:
      form=formFiles()
   return render(request,"myapp/uploud.html",{"form":form})


def edit(request,id):
    product=get_object_or_404(Product,pk=id)
    if request.method == "POST":
        form=formProduct(request.POST,request.FILES,instance=product)
        if form.is_valid():
         form.save()
         return redirect("list_view")
    else:
     form=formProduct(instance=product)
    return render(request, "myapp/edit.html", {"form":form}) 

def delete(request,id):
    product=get_object_or_404(Product,pk=id)
    if request.method == "POST":
       product.delete()
       return redirect("list_view")
    
    return render(request, "myapp/delete.html", {"product":product}) 


def getByCategoryId(request,category_id):
    category_list=list(data.keys())
  
    if category_id>len(category_list):
     return HttpResponseNotFound("yanlış kategori secimi")
    
    category_text=category_list[category_id-1]
    redirect_text=reverse("category_get",args=[category_text])
    
    return redirect(redirect_text)

def getByCategory(request,categorylink):
    # try:
      products=data[categorylink]
      return render(request,"myapp/products.html",{
          "category":categorylink,
          "products":products
      })
    # except:
        # return HttpResponseNotFound("yanlış kategori secimi")


