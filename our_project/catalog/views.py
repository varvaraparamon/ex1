from django.shortcuts import render, get_object_or_404, redirect
from reviews.models import Reviews
from catalog.models import Product, Category
from django.contrib.auth.models import User 
from reviews.forms import ReviewForm 
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'catalog/home.html')

def product_list(request):
    products =  Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products' : products,
        'categories' : categories,
        }
    return render(request, 'catalog/product_list.html', context=context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Reviews.objects.filter(product=product)

    form = ReviewForm()
    
    context = {
    'product': product,
    'reviews': reviews,
    'form': form, # Обязательно передаем форму в контекст
    }
    return render(request, 'catalog/product_detail.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('catalog:product_detail', product_id)

def cart_view(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()

    products = Product.objects.filter(id__in = product_ids)
    items = []

    total_price = 0

    for p in products:
        qty = cart[str(p.id)]
        line_total = p.price * qty
        total_price += line_total
        items.append({
            'product' : p,
            'qty' : qty,
            'line_total' : line_total
        })
    
    return render(request, 'catalog/cart.html', {
        'items' : items,
        'total_price' : total_price
    })


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
    return redirect('catalog:cart_view')


def toggle_theme(request):
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'

    next_url = request.META.get('HTTP_REFERER', '/')

    response = redirect(next_url)
    
    max_age = 365*24*60*60
    response.set_cookie('theme', new_theme, max_age=max_age, httponly=False, samesite='Lax')
    
    return response

@login_required
def chat_room(request):
    return render(request, 'catalog/chat.html')
