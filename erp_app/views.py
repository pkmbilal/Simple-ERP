from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import productForm

def listProducts(request):
    allProducts = Product.objects.all()
    return render(request, 'list_products.html',{'athira':allProducts})

def addProduct(request):
    if request.method == 'POST':
        postForm=productForm(request.POST)
        if postForm.is_valid:
            postForm.save()
            form = productForm()
            return render(request, 'add_product.html',{'form':form})
    else:
        form={'form':productForm()}
        return render(request,'add_product.html',form)
    
def updateProduct(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        formdata = productForm(request.POST,instance=product)
        if formdata.is_valid():
            formdata.save()
            return redirect('products')
       
    form = productForm(instance=product)
    return render(request,'update_product.html',{'form':form})
    
def deleteProduct(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products')