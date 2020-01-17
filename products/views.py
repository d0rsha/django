from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm, RawProductForm
from .models import Product


# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product/products.html", context)


def render_initial_data(request):
    initial_data = {
        'title': "My awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,
                       initial=initial_data, instance=obj)
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def dynamic_lookup_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
    }
    return render(request, "product/detail.html", context)


# def product_create_view(request):
#     form = RawProductForm()

#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         object_title = request.POST.get('title')
#         # Product.objects.create(title=object_title)
#     if form.is_valid():
#         # Data is good
#         print(form.cleaned_data)
#         Product.objects.create(**form.cleaned_data)

#         form.save()
#     else:
#         print(form.errors)

#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    else:
        print("COULD NOT DELETE")
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)
