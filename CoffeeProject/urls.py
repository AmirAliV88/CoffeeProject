from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('DjangoAdminPanel/', admin.site.urls),
    path('ProductsView/', views.ProductsView.as_view(), name="products"),
    path('Home/', views.HomeView.as_view(), name="HomeAPI"),
]
