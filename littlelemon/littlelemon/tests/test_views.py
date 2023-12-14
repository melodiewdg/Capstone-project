from django.test import TestCase, Client
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="ChocolateCake", price=10, inventory=50)
        Menu.objects.create(title="Sashimi", price=15, inventory=20)
        
        
        
    def test_getall(self):
        url=reverse('menu')
        response = self.client.get(url)
        
        
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)