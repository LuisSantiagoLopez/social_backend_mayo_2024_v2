from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from antros.models import Antro, MenuItem
from reservations.models import Reservation, ReservationItem

User = get_user_model()

class ReservationTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.antro = Antro.objects.create(
            name="Antro 1",
            description="Description for Antro 1",
            contact="Contact 1",
            approved=True,
            category="Techno",
            cost="$"
        )
        cls.menu_item1 = MenuItem.objects.create(
            name="Item 1",
            description="Description for Item 1",
            category="Food",
            price=10.00,
            antro=cls.antro
        )
        cls.menu_item2 = MenuItem.objects.create(
            name="Item 2",
            description="Description for Item 2",
            category="Drink",
            price=5.00,
            antro=cls.antro
        )
        cls.client.login(username='testuser', password='testpass')

    def test_create_reservation(self):
        self.client.login(username='testuser', password='testpass')
        url = '/reservations/'
        data = {
            "antro": self.antro.id,
            "user": self.user.id,
            "cost": 30.00,
            "items": [
                {"menu_item": self.menu_item1.id, "quantity": 2},
                {"menu_item": self.menu_item2.id, "quantity": 1}
            ]
        }
        response = self.client.post(url, data, format='json')
        print(response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(ReservationItem.objects.count(), 2)

    def test_retrieve_reservation(self):
        self.client.login(username='testuser', password='testpass')
        reservation = Reservation.objects.create(
            antro=self.antro, user=self.user, cost=30.00
        )
        ReservationItem.objects.create(reservation=reservation, menu_item=self.menu_item1, quantity=2)
        ReservationItem.objects.create(reservation=reservation, menu_item=self.menu_item2, quantity=1)
        
        url = f'/reservations/{reservation.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], reservation.id)

    def test_update_reservation(self):
        self.client.login(username='testuser', password='testpass')
        reservation = Reservation.objects.create(
            antro=self.antro, user=self.user, cost=30.00
        )
        ReservationItem.objects.create(reservation=reservation, menu_item=self.menu_item1, quantity=2)
        
        url = f'/reservations/{reservation.id}/'
        data = {
            "antro": self.antro.id,
            "user": self.user.id,
            "cost": 50.00,
            "items": [
                {"menu_item": self.menu_item1.id, "quantity": 3},
                {"menu_item": self.menu_item2.id, "quantity": 2}
            ]
        }
        response = self.client.put(url, data, content_type='application/json')  # Ensure content type
        print(response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cost'], '50.00')
        self.assertEqual(ReservationItem.objects.count(), 2)

    def test_delete_reservation(self):
        self.client.login(username='testuser', password='testpass')
        reservation = Reservation.objects.create(
            antro=self.antro, user=self.user, cost=30.00
        )
        ReservationItem.objects.create(reservation=reservation, menu_item=self.menu_item1, quantity=2)
        
        url = f'/reservations/{reservation.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reservation.objects.count(), 0)
        self.assertEqual(ReservationItem.objects.count(), 0)

    def test_invalid_reservation_data(self):
        self.client.login(username='testuser', password='testpass')
        url = '/reservations/'
        data = {
            "antro": self.antro.id,
            "user": self.user.id,
            "cost": "invalid_cost",  # invalid cost format
            "items": [
                {"menu_item": self.menu_item1.id, "quantity": 2}
            ]
        }
        response = self.client.post(url, data, format='json')
        print(response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_reservation(self):
        self.client.login(username='testuser', password='testpass')
        url = '/reservations/'
        data = {
            "antro": self.antro.id,
            "user": self.user.id,
            "cost": 30.00,
            "items": [
                {"menu_item": self.menu_item1.id, "quantity": 2},
                {"menu_item": self.menu_item2.id, "quantity": 1}
            ]
        }
        response = self.client.post(url, data, format='json')
        print("Response Status Code:", response.status_code)  # Debugging line
        print("Response Content:", response.content)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(ReservationItem.objects.count(), 2)

