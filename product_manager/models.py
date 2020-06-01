from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from PIL import Image


class Product(models.Model):

    name = models.CharField(max_length=155)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    description = models.TextField(max_length=240)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image= models.ImageField(default='new.jpg',blank=True, upload_to = 'product_img')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return u'%s' % self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def imageURL(self):
        try:
		       url = self.image.url
        except:
	           url = ''
        return url

    def get_absolute_url(self):
        return reverse('product_manager_product_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('product_manager_product_update', args=(self.slug,))

    def get_delete_url(self):
        return reverse('product_manager_product_delete', args=(self.slug,))
