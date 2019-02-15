from django.shortcuts import render

def home(request): #Parameter "request" comes from urls module
    products = ["Cherries", "Apples", "Tangerines", "Guava", "Kumquat"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)