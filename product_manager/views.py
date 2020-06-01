""" This file controls the views for Products and Categories inside product_manager. """

# Django imports
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Project imports
from .models import Product
from .forms import ProductForm


# class IndexView(ListView):
#     """ This index view displays the last ten products created. """
#     template_name = 'product_manager/index.html'
#
#     def get_queryset(self):
#             """ Return the last ten products. """
#             return Product.objects.order_by('-id')[:10]


class ProductListView(ListView):
    """ Allows you to list all products. """
    model = Product


# class ProductCreateView(CreateView):
#     """ Allows you to create a product (linked to forms). """
#     model = Product
#     form_class = ProductForm

def ProductCreateView(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('success')

        return render(request,'product_manager/product_form.html',{'form': form,})


    else:
        form = ProductForm()
        return render(request,'product_manager/product_form.html',{'form': form,})


def success(request):
    return redirect('store')

class ProductDetailView(DetailView):
    """ Allows you to view detailed information about an object in Product. """
    model = Product


class ProductDeleteView(DeleteView):
    """ Allows you to delete a product. """
    model = Product
    success_url = reverse_lazy('product_manager_product_list')


class ProductUpdateView(UpdateView):
    """ Allows you to update a product's details. """
    model = Product
    form_class = ProductForm
