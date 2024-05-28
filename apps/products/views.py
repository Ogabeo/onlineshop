from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.products.models import Product, Category, Brand, ProductSize, Size, Contact, About
from django.core.paginator import Paginator
from django.db.models import Q

class HomePageView(View):
    def get(self, request):
        products=Product.objects.all().filter(is_active=True)
        first_about = About.objects.first()
        featured_products=products.order_by('?')[:16]
        famous=products.filter(status='Sale')
        latest_products = products.filter(status='New').order_by('?')[:8]
        random_news=products.order_by('?')[:5]
        random_product=products.order_by('-percentage').order_by('?')[:2]
        new_products=products.filter(status='New').order_by('?')[:3]
        famous_news=products.filter(status='New').order_by('?')[:3]
        hot_news=products.filter(status='Hot').order_by('?')[:3]
        context ={
            'featured_products':featured_products,
            'latest_products':latest_products,
            'random_news':random_news,
            'famous':famous,
            'random_product':random_product,
            'new_products':new_products,
            'famous_news':famous_news,
            'hot_news':hot_news,
            # 'brands':brands,
            'first_about':first_about
        }
        return render(request, 'products/index.html', context)

 

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

        return render(request, "products/shop.html", context)

class DetailView(View):
    def get(self, request, uuid):
        this_product =get_object_or_404(Product, id=uuid)
              
        product_colors = this_product.sizes.all().distinct()
        product_sizes= this_product.sizes.all().values('size').distinct()
        pre_sizes = Size.objects.filter(id__in = product_sizes )
        product_comments = this_product.reviews.all().filter(is_active = True).order_by('-id')[:3]
        products_on_this_category = Product.objects.filter(is_active = True, categories=this_product.categories.all().last())
        
        # print(this_product)
        # print(product_colors)

        context = {
            'this_product':this_product,
            'product_colors':product_colors,
            'product_sizes':pre_sizes,
            'product_comments':product_comments,
            'products_on_this_category':products_on_this_category
        }
    
        return render(request, 'products/detail.html', context)



class CategoryProductsView(View):
    def get(self, request, uuid):
        ctg = Category.objects.get(id=uuid)
        category_news = Product.objects.all().filter(is_active=True, categories=ctg)
        print(category_news)
        context = {
            'ctg':ctg,
            'category_news':category_news
        }
        return render(request, 'products/category_products.html', context)

class ContactView(View):
    def get(self, request):
        return render(request, 'products/contact.html')
    
    def post(self, request):
        data = request.POST
        contact = Contact()
        contact.firstname = data.get('firstname')
        contact.email = data.get('email')
        contact.phone = data.get('phone')
        contact.subject = data.get('subject')
        contact.message = data.get('message')

        contact.save()

        return redirect('home')

# class About(View):
#     def get(self, request):
#         first_about = About.objects.first()
#         address = first_about.address

#         context = {
#             'address':address
#         }
#         return render(request, 'products/index.html', context)
    


class BrandProducts(View):
    def get(self, request, uuid):
        brand = Brand.objects.all().filter(is_active = True, id=uuid)
        
        brands = Brand.objects.all().filter(is_active = True)

        brand_products = Product.objects.filter(is_active = True, products=brand)
        print(brand_products)
        print(brand)
        context = {
            'brand':brand,
            'brands':brands,
            'brand_products':brand_products
        }  
        return render(request, 'products/index.html', context) 
# class ShopBrandView(View):

#     def get(self, request, uuid):
#         brand= get_object_or_404(Brand, id=uuid)
#         brands = Brand.objects.all()

#         brand_products=brand.products.filter(is_active=True)  
#         print(brand_products)
#         page_size=request.GET.get('page_size', 10)
#         paginator = Paginator(brand_products, page_size)
#         page = request.GET.get('page', 1)
#         page_obj = paginator.page(page)
#         context = {
#             'products_all':page_obj,
#             'page_size':page_size,
#             'brands':brands
#         }

#         return render(request, "products/index.html", context)