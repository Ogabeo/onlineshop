from django.shortcuts import render, get_object_or_404
from django.views import View
from apps.products.models import Product, Category, Brand
from django.core.paginator import Paginator
from django.db.models import Q
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

        sort_by =request.GET.get('sort_by', '?')

        categories = Category.objects.all().filter(is_active=True, parent=None)

        products_all = Product.objects.all().filter(is_active = True).order_by(sort_by)


        
        


        search = request.GET.get('search', '')
        if search:
            products_all = products_all.filter(Q(title__icontains = search) | Q(description__icontains = search) ).order_by(sort_by)
            
        print(search)
        


        page_size=request.GET.get('page_size', 10)
        if page_size == 'all':
            page_size = products_all.count()

        paginator = Paginator(products_all, page_size)

        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)



        context = {
            'categories':categories,
            'products_all':page_obj,
            'page_size':page_size,
            'search':search,

        }

        return render(request, "products/shop.html", context)
    

class ShopCategoryView(View):

    def get(self, request, uuid):
        ctg= get_object_or_404(Category, id=uuid)
        categories = Category.objects.all().filter(is_active=True, parent=ctg)

        if not categories:
            categories=Category.objects.all().filter(is_active=True, level=1 )
        

        ctg_products=ctg.products.filter(is_active=True)     
        page_size=request.GET.get('page_size', 10)
        paginator = Paginator(ctg_products, page_size)
        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)
        context = {
            'products_all':page_obj,
            'page_size':page_size,
            'categories':categories
        }

        print(page_obj)
        # print(categories)
        return render(request, "products/shop.html", context)

class DetailView(View):
    def get(self, request, uuid):
        this_product =get_object_or_404(Product, id=uuid)

        print(this_product)
        context = {
            'this_product':this_product
        }

        return render(request, 'products/detail.html', context)
