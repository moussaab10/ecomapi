# from django.shortcuts import render
# from django.http import JsonResponse
# # decorators : ta3 autorisation 
# from rest_framework.decorators import api_view,permission_classes
# # type de @permission_classes
# from rest_framework.permissions import IsAuthenticated,IsAdminUser


# from rest_framework.response import Response

# from .models import Product
# from .products import products
# from django.contrib.auth.models import User

# from .serializers import ProductSerializer,UserSerializer,UserSerializerWithToken
# # from .products import products
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth.hashers import make_password
# from rest_framework import status

 

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/products/',
#         '/api/products/create/',
#         '/api/products/upload/',
#         '/api/products/<id>/reviews/',
#         '/api/products/top/',
#         '/api/products/<id>/',
#         '/api/products/delete/<id>/',
#         '/api/products/<uploade>/<id>/',
#     ]
#     return Response(routes)


