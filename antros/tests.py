from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.gis.geos import Point
from .models import Antro, MenuItem, Review

User = get_user_model()

class AntroTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="user1", password="password")
        cls.user2 = User.objects.create_user(username="user2", password="password")
        cls.antros_user1 = [
            Antro.objects.create(
                user=cls.user1,
                name="Antro 1",
                description="Description for Antro 1",
                contact="Contact 1",
                approved=True,
                category="Techno",
                cost="$"
            ),
            Antro.objects.create(
                user=cls.user1,
                name="Antro 2",
                description="Description for Antro 2",
                contact="Contact 2",
                approved=False,
                category="Luxury",
                cost="$$$"
            )
        ]
        cls.antros_user2 = [
            Antro.objects.create(
                user=cls.user2,
                name="Antro 3",
                description="Description for Antro 3",
                contact="Contact 3",
                approved=True,
                category="Pop",
                cost="$$"
            )
        ]

    def setUp(self):
        self.client = APIClient()
        self.client.login(username='user1', password='password')

    def test_antros_content(self):
        for antro in self.antros_user1 + self.antros_user2:
            self.assertIsInstance(antro.name, str)
            self.assertIsInstance(antro.description, str)
            self.assertIsInstance(antro.contact, str)
            self.assertIsInstance(antro.approved, bool)
            self.assertIsInstance(antro.category, str)
            self.assertIsInstance(antro.cost, str)
            self.assertIn(antro.cost, ['$', '$$', '$$$'])
            self.assertEqual(str(antro), antro.name)

    def test_create_antros_with_location(self):
        data = {
            'user': self.user1.id,
            'name': 'Antro with Location',
            'description': 'Description for Antro with Location',
            'contact': 'Contact with Location',
            'approved': True,
            'category': 'Techno',
            'cost': '$',
            'latitude': 25.7617,
            'longitude': -80.1918
        }
        response = self.client.post('/antros-list/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        antro = Antro.objects.get(id=response.data['id'])
        self.assertEqual(antro.location, Point(-80.1918, 25.7617, srid=4326))

    def test_update_antros_with_location(self):
        antro = self.antros_user1[0]
        data = {
            'name': antro.name,
            'description': antro.description,
            'contact': antro.contact,
            'approved': antro.approved,
            'category': antro.category,
            'cost': antro.cost,
            'latitude': 25.7617,
            'longitude': -80.1918
        }
        response = self.client.put(f'/antros-list/{antro.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        antro.refresh_from_db()
        self.assertEqual(antro.location, Point(-80.1918, 25.7617, srid=4326))

class MenuItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="user1", password="password")
        cls.user2 = User.objects.create_user(username="user2", password="password")
        cls.antro_user1 = Antro.objects.create(
            user=cls.user1,
            name="Antro 1",
            description="Description for Antro 1",
            contact="Contact 1",
            approved=True,
            category="Techno",
            cost="$"
        )
        cls.antro_user2 = Antro.objects.create(
            user=cls.user2,
            name="Antro 2",
            description="Description for Antro 2",
            contact="Contact 2",
            approved=True,
            category="Pop",
            cost="$$"
        )
        cls.menu_item = MenuItem.objects.create(
            name="Menu Item 1",
            description="Description for Menu Item 1",
            category="Food",
            price=9.99,
            antro=cls.antro_user1
        )

    def test_menu_item_content(self):
        self.assertEqual(self.menu_item.name, "Menu Item 1")
        self.assertEqual(self.menu_item.description, "Description for Menu Item 1")
        self.assertEqual(self.menu_item.category, "Food")
        self.assertEqual(self.menu_item.price, 9.99)
        self.assertEqual(self.menu_item.antro, self.antro_user1)
        self.assertEqual(str(self.menu_item), self.menu_item.name)

    def test_user_can_create_menu_item_for_own_antro(self):
        client = APIClient()
        client.login(username='user1', password='password')
        url = '/antros/menu-items/'
        data = {
            "name": "Menu Item 2",
            "description": "Description for Menu Item 2",
            "category": "Drink",
            "price": 5.99,
            "antro": self.antro_user1.id
        }
        response = client.post(url, data, format='json')
        print("Response Status Code:", response.status_code)  # Debugging line
        print("Response Content:", response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_create_menu_item_for_others_antro(self):
        client = APIClient()
        client.login(username='user1', password='password')
        url = '/antros/menu-items/'
        data = {
            "name": "Menu Item 3",
            "description": "Description for Menu Item 3",
            "category": "Dessert",
            "price": 7.99,
            "antro": self.antro_user2.id
        }
        response = client.post(url, data, format='json')
        print("Response Status Code:", response.status_code)  # Debugging line
        print("Response Content:", response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ReviewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="password"
        )
        cls.antro = Antro.objects.create(
            user=cls.user,
            name="Antro 1",
            description="Description for Antro 1",
            contact="Contact 1",
            approved=True,
            category="Techno",
            cost="$"
        )
        cls.review = Review.objects.create(
            user=cls.user,
            rating=5,
            comment="Great place!",
            antro=cls.antro
        )

    def test_review_content(self):
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great place!")
        self.assertEqual(self.review.antro, self.antro)
        self.assertEqual(str(self.review), self.review.comment)
