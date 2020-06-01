import json
from .models import *

def cookieWish(request):

	#Create empty wish for now for non-logged in user
	try:
		wish = json.loads(request.COOKIES['wish'])
	except:
		wish = {}
		print('CART:', wish)

	items = []
	wishlist = {'get_wish_total':0, 'get_wish_items':0}
	wishItems = wishlist['get_wish_items']

	for i in wish:
		#We use try block to prevent items in wish that may have been removed from causing error
		try:
			wishItems += wish[i]['quantity']

			product = Product.objects.get(id=i)
			total = (product.price * wish[i]['quantity'])

			wishlist['get_wish_total'] += total
			wishlist['get_wish_items'] += wish[i]['quantity']

			item = {
				'id':product.id,
				'product':{'id':product.id,'name':product.name, 'price':product.price,
				'imageURL':product.imageURL}, 'quantity':wish[i]['quantity'],
				'get_total':total,
				}
			items.append(item)

		except:
			pass

	return {'wishItems':wishItems ,'wishlist':wishlist, 'items':items}

def wishData(request):
	if request.user.is_authenticated:
		customer = request.user
		wishlist, created = Wishlist.objects.get_or_create(customer=customer)
		items = wishlist.wishlistitem_set.all()
		wishItems = wishlist.get_wish_items
	else:
		cookieData = cookieWish(request)
		wishItems = cookieData['wishItems']
		wishlist = cookieData['wishlist']
		items = cookieData['items']

	return {'wishItems':wishItems ,'wishlist':wishlist, 'items':items}

#
# def guestWishlist(request, data):
# 	name = data['form']['name']
# 	email = data['form']['email']
#
# 	cookieData = cookieWish(request)
# 	items = cookieData['items']
#
# 	customer, created = Customer.objects.get_or_create(
# 			email=email,
# 			)
# 	customer.name = name
# 	customer.save()
#
# 	wishlist = Wishlist.objects.create(
# 		customer=customer,
#
# 		)
#
# 	for item in items:
# 		product = Product.objects.get(id=item['id'])
# 		wishlistItem = WishlistItem.objects.create(
# 			product=product,
# 			wishlist=wishlist,
# 			quantity=item['quantity'],
# 		)
# 	return customer, wishlist
