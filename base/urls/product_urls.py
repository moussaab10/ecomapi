from django.urls import path
from base.views import product_views as views


urlpatterns = [
    path('', views.getProducts, name="products"),
    path('<str:pk>/reviews/', views.crsateProductReview, name="product-review"),
    path('<str:pk>/', views.getProduct, name="product"),
    path('delete/<str:pk>/', views.deleteProduct, name="product"),

]
