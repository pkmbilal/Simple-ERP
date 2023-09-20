from django.urls import path
from . import views

urlpatterns = [
    path('',views.listProducts,name='products'),
    path('addProduct/',views.addProduct,name='addproduct'),
    path('updateProduct/<int:id>/',views.updateProduct,name='updateproduct'),
    path('deleteProduct/<int:id>/',views.deleteProduct,name='deleteproduct'),
]