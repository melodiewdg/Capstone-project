from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def menu_test(self):
        item = Menu.objects.create(title="IceCream", price=8, inventory=100)
        self.assertEqual(item, "IceCream : 8")

