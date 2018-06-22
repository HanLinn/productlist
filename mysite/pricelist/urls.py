from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_name_id>',
         views.productlist, name='productlist'),
    path('category/product_update/<int:id>/', views.product_update, name="product_update")
]
