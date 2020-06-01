from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieWish, wishData
from django.contrib.auth.decorators import login_required


def store(request):
	data = wishData(request)

	wishItems = data['wishItems']
	wishlist = data['wishlist']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'wishItems':wishItems}
	return render(request, 'wishlists/store.html', context)

@login_required(login_url="/login_user/")
def view_wishlist(request):
	data = wishData(request)

	wishItems = data['wishItems']
	wishlist = data['wishlist']
	items = data['items']

	context = {'items':items, 'wishlist':wishlist, 'wishItems':wishItems}
	return render(request, 'wishlists/wish.html', context)


@login_required(login_url="/login_user/")
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	wishlist, created = Wishlist.objects.get_or_create(customer=customer)

	wishlistItem, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)

	if action == 'add':
		wishlistItem.quantity = (wishlistItem.quantity + 1)
	elif action == 'remove':
		wishlistItem.quantity = (wishlistItem.quantity - 1)

	wishlistItem.save()

	if wishlistItem.quantity <= 0:
		wishlistItem.delete()

	return JsonResponse('Item was added', safe=False)
