from django.urls import path
from .views import ProductList, ProductDetail, RegisterView, CategoryList, OrderCreateView

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('register/', RegisterView.as_view()),
    path('categories/', CategoryList.as_view()),
    path('orders/', OrderCreateView.as_view()),
]