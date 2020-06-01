""" This file creates test data for Product and Category using the autofixture class. """

from django.conf import settings
from django.db import models as models
from django.db.models import *
from .models import Product
from autofixture import generators, register, AutoFixture

class ProductAutoFixture(AutoFixture):
    field_values = {
        'name': generators.ChoicesGenerator(
            values=(
                "Eggs",
                "Cheese",
                "Bacon",
                "Milk",
                "Oranges",
                "Apples",
                "Pears",
                "Lemons"
            )
        ),
        'description': generators.ChoicesGenerator(
            values=(
                "A type of food.",
                "Something to consume.",
                "Very tasty!",
                "Healthy.",
                "Now on sale!"
            )
        ),
        'price': generators.ChoicesGenerator(
            values=(
                '15.45',
                '2.00',
                '14.00',
                '10.05'
            )
        ),
    }

register(Product, ProductAutoFixture)
