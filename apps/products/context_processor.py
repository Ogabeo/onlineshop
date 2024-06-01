from .models import Category, Product, Brand, About

def category_context(request):
    first_about = About.objects.first()

    categories = Category.objects.all().filter(is_active=True, parent=None)
    mega_menu = categories[:3]
    brands= Brand.objects.order_by('?')[:6]
    new_products = Product.objects.filter(is_active=True, status="New" )[:3]
    last_ctgs=Category.objects.all().filter(is_active=True, children__isnull=True)
    sevimlilar = 0
    cards = 0
    if request.user.is_authenticated:
        sevimlilar = request.user.sevimlilar.all().count()
        cards = request.user.orders.all().filter(status=False).count()

    context={
        'categories':categories,
        'first_about':first_about,
        'new_products':new_products,
        'mega_menu':mega_menu,
        'last_ctgs':last_ctgs,
        'sevimlilar':sevimlilar,
        'cards':cards,
        'brands':brands
        
    }
    
    return context


