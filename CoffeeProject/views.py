from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

class HomeView(View):
   def get(self, request):
      # messages.success(request, " ✨ روز n مبارک ✨ ", "info") #? dynamic notifcation
      pass

