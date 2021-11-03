from django.shortcuts import redirect, render
from home.models import Product, ProductImage


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    products = Product.objects.all()
    params = {
        'products': products,
    }
    return render(request, 'home/home.html', params)


def select_configuration(request):
    return render(request, 'home/laptop/select-configuration.html')


def products_view(request, pk):
    get_product = Product.objects.get(id=pk)
    more_images = ProductImage.objects.filter(product=get_product)
    params = {
        'product': get_product,
        'more_images': more_images,
    }
    return render(request, 'home/view.html', params)


def light_weight(request):
    return render(request, 'home/laptop/light-weight.html')


def medium(request):
    return render(request, 'home/laptop/medium.html')


def asus(request):
    return render(request, 'home/laptop/view/asus.html')


def alienware(request):
    return render(request, 'home/laptop/view/alienware.html')


def as_invoice(request):
    return render(request, 'home/laptop/view/asus-invoice.html')


def al_invoice(request):
    return render(request, 'home/laptop/view/alienware-invoice.html')


def order_placed(request):
    return render(request, 'home/order-placed.html')
