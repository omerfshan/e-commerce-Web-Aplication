from django import forms
from .models import Product
# class formProduct(forms.Form):
#     product_name = forms.CharField(max_length=20,label="ürün adi",min_length=3,
#     error_messages={
#         "max_lenght":"max 20 karekter",
#         "min_lenght":"min 3 karekter"},
        
#         widget=forms.TextInput(attrs={"class":"form-control"}))

#     price = forms.DecimalField(widget=forms.TextInput(attrs={"class":"form-control"}),max_digits=20,decimal_places=2,label="ürün fiyat",min_value=10,max_value=1000000) 
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),)
#     slug=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="url")



class formProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'slug','image')  # 'field' yerine 'fields' olmalı.
        error_messages={
           "name":{ "blank": "Ürün adı boş bırakılamaz.",
            "max_length": "Ürün adı en fazla 50 karakter olabilir."}
        }
        labels = {
            "name": "Ürün Adı",
            "price": "Ürün Fiyatı",
            "description": "Ürün Açıklaması",
            "slug": "Ürün URL"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),  # 'Widgets' yerine 'forms' kullanılmalı.
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }

class formFiles(forms.Form):
     image=forms.FileField()
    