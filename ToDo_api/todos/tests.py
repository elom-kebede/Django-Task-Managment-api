from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class TestListCreateview(APITestCase):

    def authenticate(self):
        self.client.post(reverse('register'), {
            'username': 'testuser', 'email': 'test@gmail.com', 'password': 'testpassword'})
        
        response = self.client.post(reverse('login'), {
            'email': 'test@gmail.com', 'password': 'testpassword'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

        token_tuple = response.data.get('token', None)  
        self.assertIsNotNone(token_tuple, "Token was not returned from login.")  # Ensure token exists

    # Extract token from tuple
        token = token_tuple[0] if isinstance(token_tuple, tuple) else token_tuple  

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        
         
        

    def test_create_task(self):
        self.authenticate()
        response = self.client.post(reverse('task-list-create'), {
            'title': 'Test Task',
            'description': 'Test Task Description'
           
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)