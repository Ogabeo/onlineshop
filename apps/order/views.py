from django.shortcuts import render, redirect
from .models import Sevimlilar, Order, Payment
from apps.products.models import Product
from django.views import View
from django.db.models import Q
from .forms import PaymentForm

# Create your views here.

class AddToFavorite(View):
    def post(self, request):
        user = request.user 
        
        product = request.POST.get('product_id')
        print(product)
        product = Product.objects.get(id = product)
        Sevimlilar.objects.create(user=user, product = product)
        return redirect('detail', uuid = product.id)
    
class FavoriteView(View):
    def get(self, request):
        user = request.user
        sevimlilar = Sevimlilar.objects.filter(user=user)
        context = {
            'sevimlilar':sevimlilar
        }

        return render(request, 'products/shop-wishlist.html', context)

def delete_favorite(request, uuid):
    sevimlilar = Sevimlilar.objects.get(id=uuid)
    sevimlilar.delete()
    return redirect('favorite')

def add_shop_card(request, uuid):
    url = request.META.get('HTTP_REFERER')
    user = request.user
    product=Product.objects.get(id=uuid)
    Order.objects.create(user=user, product=product)
    return redirect(url)


class ShopCartView(View):
    def get(self, request):
        user = request.user
        OrderedProducts = Order.objects.filter(Q(user=user) & Q(status =False))
        context = {
            'OrderedProducts':OrderedProducts
        } 
        return render(request, 'products/shop-cart.html', context)

    


def delete_shop_card(request, uuid):
    order = Order.objects.get(id=uuid)
    order.delete()
    return redirect('shop_cart')

def delete_all_shop_card(request):
    AllOrderedProducts = Order.objects.all()
    AllOrderedProducts.delete()
    return redirect('shop_cart')

class ShopAddress(View):
    def get(self, request):
        form = PaymentForm()
        context = {
            'form':form
        }
        return render(request, 'products/shop_address.html', context)
    def post(self, request):
        user = request.user
        OrderedProducts = Order.objects.filter(Q(user=user) & Q(status =False))
        form = PaymentForm(request.POST)
        print("sdfdsfsdfsdf")
        
        if form.is_valid():
            print("======================")
            payment = form.save(commit=False)
            payment.save()
            payment.order.set(OrderedProducts)
            
        return redirect('payment', uuid=payment.id)
        

class PaymentView(View):
    def get(self, request, uuid):
        payment = Payment.objects.get(id=uuid)
        context = {
            'payment':payment
        }
        return render(request, 'products/card_totals.html', context)
    