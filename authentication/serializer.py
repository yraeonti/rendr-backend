from rest_framework import serializers
from authentication.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'company_name', 'email', 'password']

    def validate_password(self, value):
        """
        Check password length.
        """

        if len(value) < 6:
            raise serializers.ValidationError("Password is less than 6 characters")
        return value
    



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        print(user)
        # Add custom claims
        token['user_id'] = user.id
        token['name'] = user.name
        token['email'] = user.email

        return token