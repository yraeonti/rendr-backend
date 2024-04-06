from rest_framework import generics
from authentication.models import User
from authentication.serializer import AuthSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


class Signup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer

class MyTokenTokenObtainPairView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = MyTokenObtainPairSerializer



        
 