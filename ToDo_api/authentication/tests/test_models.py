from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user=User.objects.create_user('ella','ella@gmail.com','ella123')
        self.assertFalse(user.is_staff)
        self.assertEqual(user.username, 'ella')

    def test_create_superuser(self):
        user = User.objects.create_superuser('neba', 'neba@gmial.com', 'neba123')
        self.assertTrue(user.is_staff)

    def test_raises_error_noUsername(self):
        self.assertRaises(ValueError,User.objects.create_user,username='',email='ella@gmial.com', password='ella123')
    
    def test_raises_error_noEmail (self):
        self.assertRaises(ValueError,User.objects.create_user,username='ella', email='', password='ella123')
    
    def test_staff_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='ella',email='ella@gmail.com', password='ella123', is_staff=False)
    def test_is_superUser_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='ella',email='ella@gmail.com', password='ella123', is_superuser=False)