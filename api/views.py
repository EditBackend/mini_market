from rest_framework import generics, permissions
from .models import Product, Category, Order
from .serializers import ProductSerializer, UserSerializer, CategorySerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Mahsulotlar ro'yxati va qidiruv
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Registratsiya
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)