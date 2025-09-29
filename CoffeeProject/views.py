from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Product

class HomeView(View):
   def get(self, request):
      messages = []
      # messages.append(("happy", " ✨ روز n مبارک ✨ ")) #? dynamic notifcation
      RequestData = {"messages":messages} #? more API datas...
      return HttpResponse(RequestData)

class DeleteProductView(View):
   def get(self, request, id):
      p = Product.Objects.filter(id=id)
      if p: 
         p.delete()
         return HttpResponse({"status":"success", "code":200})
      return HttpResponse({"status":"error", "code":500})

class CreateProductView(View):
   def post(self, request):
      try:
         name = request.query.get("name", None) #? اسم
         description = request.query.get("description", "") #? توضیحات
         price = request.query.get("price", 0) #? قیمت | قیمت باید بین 0 و یک میلیون باشه
         if name !=None & description !="" & 1000000 > price >= 0:
            P = Product.objects.Create(name=name, description=description, price=price)
         return HttpResponse({"status":"success", "code":200})
      except:
         return HttpResponse({"status":"error", "code":500})


class ProductsView(View):
   def get(self, request):
      pass




