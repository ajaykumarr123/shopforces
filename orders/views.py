from django.shortcuts import render
from .models import OrderItem , Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login_user/")
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            #order_created.delay(order.id)
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

class order_history(ListView):
    model= Order

@login_required(login_url="/login_user/")
def order_detail(request , id):
    order=Order.objects.get(id=id)
    items=OrderItem.objects.all()
    return render(request, 'orders/order_detail.html', {'order': order,'items':items})
