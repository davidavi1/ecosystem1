from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Product, ProductCategory,Zakaz
from .forms import ZakazForm

class ProductListView(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = ProductCategory.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.all().order_by('-id')
        context["category"] = ProductCategory.objects.all()
        return context


def BuyProduct(request,pk):
    current_product = Product.objects.filter(pk=pk)
    category = ProductCategory.objects.all()
    if request.method == 'POST':
        form = ZakazForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ZakazForm()


    return render(request,'zakaz.html',{'current':current_product,'form':form,'category':category})


def CategoryView(request, pk):
    current = ProductCategory.objects.get(pk=pk)
    product = Product.objects.filter(category=pk)
    category = ProductCategory.objects.all()
    return render(request, 'product/categories.html', {'current': current, 'product': product,'category':category})

