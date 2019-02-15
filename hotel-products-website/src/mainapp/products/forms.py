from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm): #Ensures that the user data matches the form of "Product"
    class Meta: #Subclass
        model = Product
        fields = '__all__' #Gets all fields from user