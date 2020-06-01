from django.db import models
from product_manager.models import Product
from django.contrib.auth.models import User
from accounts.models import Customer


class Wishlist(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	date = models.DateTimeField(auto_now_add=True)
	#items = models.ManyToManyField(Wishlist,related_name="q1")

	def __str__(self):
		return str(self.id)

	@property
	def get_wish_total(self):
		wishlistitems = self.wishlistitem_set.all()
		total = sum([item.get_total for item in wishlistitems])
		return total

	@property
	def get_wish_items(self):
		wishlistitems = self.wishlistitem_set.all()
		total = sum([item.quantity for item in wishlistitems])
		return total

class WishlistItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	wishlist = models.ForeignKey(Wishlist, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
