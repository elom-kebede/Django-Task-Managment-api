from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=65, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email','password','token']

        read_only_fields = ['token']