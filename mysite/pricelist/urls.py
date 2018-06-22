from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_name_id>',
         views.productlist, name='productlist'),
    path('category/product_update/<int:id>/', views.product_update, name="product_update"),
    path('category/product_create/', views.product_create, name="product_create"),
    path('category/product_delete/<int:id>/',views.product_delete,name="product_delete")
]
