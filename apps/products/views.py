from django.shortcuts import render
from django.views import View
from apps.products.models import Product, Category, Brand
from django.core.paginator import Paginator

class HomePageView(View):
    def get(self, request):
        products=Product.objects.all().filter(is_active=True)
        featured_products=products.order_by('?')[:16]
        famous=products.filter(status='Sale')
        latest_products = products.filter(status='New').order_by('?')[:8]
        random_news=products.order_by('?')[:5]
        random_product=products.order_by('-percentage').order_by('?')[:2]
        new_products=products.filter(status='New').order_by('?')[:3]
        famous_news=products.filter(status='New').order_by('?')[:3]
        hot_news=products.filter(status='Hot').order_by('?')[:3]
        brands = Brand.objects.all().filter(is_active=True)
        
        context ={
            'featured_products':featured_products,
            'latest_products':latest_products,
            'random_news':random_news,
            'famous':famous,
            'random_product':random_product,
            'new_products':new_products,
            'famous_news':famous_news,
            'hot_news':hot_news,
            'brands': brands

        }
        return render(request, 'products/index.html', context)
    
class CategoryProductsView(View):
    def get(self, request):
        # ctg = Category.objects.get(id=id)
        # category_products=ctg.products.all()
        
        return render(request, 'products/category_products.html')
    
class ShopAllView(View):
    def get(self, request):
        products_all = Product.objects.all().filter(is_active = True)

        page_size=request.GET.get('page_size', 10)
        paginator = Paginator(products_all, page_size)

        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)
        print(page_size)



        context = {
            'products_all':page_obj,
            'page_size':page_size,
        }

        return render(request, "products/shop.html", context)
    