from .models import Category, Product

def category_context(request):
    categories = Category.objects.all().filter(is_active=True, parent=None)
    mega_menu = categories[:3]
    last_ctgs=Category.objects.all().filter(is_active=True, children__isnull=True)
    sevimlilar = 0
    cards = 0
    if request.user.is_authenticated:
        sevimlilar = request.user.sevimlilar.all().count()
        cards = request.user.orders.all().filter(status=False).count()
 

    context={
        'categories':categories,
        'mega_menu':mega_menu,
        'last_ctgs':last_ctgs,
        'sevimlilar':sevimlilar,
        'cards':cards,
        
    }
    
    return context


