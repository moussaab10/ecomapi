from django.shortcuts import render
# decorators : ta3 autorisation
from rest_framework.decorators import api_view, permission_classes
# type de @permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Product, Order, OrderItem, ShippingAddress

from base.serializers import OrderSerializer, ProductSerializer
# from .products import products
from rest_framework import status
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data

    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:

        # (1) Create order

        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
        )

        # creat shipping addres
        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['addres'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['codePostal'],
            country=data['shippingAddress']['country'],
        )

        # creat oreder items
        for i in orderItems:
            product = Product.objects.get(_id=i['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )

            # update stock
            product.countInStock -= item.qty
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if(user.is_staff or order.user == user):
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return Response({'detail': 'u are not allowed to see this order'}, status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):

    user = request.user
    data = request.data

    order = Order.objects.get(_id=pk)
    order.isPaid = data['isPaid']
    order.paidAt = datetime.now()
    order.save()
    return Response('order was paid ')
