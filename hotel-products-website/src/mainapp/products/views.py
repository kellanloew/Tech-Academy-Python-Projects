from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

def admin_console(request): #Shows the product page when given a request
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk) #First 'pk' is the primarykey in the table. item stores data associated with that pk
    form = ProductForm(data=request.POST or None, instance=item) #If user gives info, make sure is POST. Save it into class instance 'form', which backfills all boxes of form with item name
    if request.method == 'POST': #If user gave us data for the database via POST method
        if form.is_valid():#If valid entry
            form2 = form.save(commit=False)
            form2.save() #saves user's entered data into database
            return redirect('admin')#Afterwards returns us to main console page
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form': form})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin')
    context = {"item": item,}
    return render(request, "products/confirmDelete.html", context)

def confirmed(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None) #Creates a form instance and binds data to it
        if form.is_valid():
            form.delete()
            return redirect('admin')
    else:
        return redirect('admin')

def createRecord(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin')
    else:
        print(form.errors)
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/createRecord.html', context)
