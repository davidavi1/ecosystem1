from django.shortcuts import render,redirect
from .forms import FeedBackForms
from .models import FeedBackModel
from product.models import ProductCategory

def FeedBackView(request):
    category = ProductCategory.objects.all()
    if request.method == 'POST':
        form = FeedBackForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedBackForms

    return render(request,'feedback/contact.html',{'form':form,'category':category})