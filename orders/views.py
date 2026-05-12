from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Cake, Branch, Order
from .serializers import CakeSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.http import JsonResponse
import json
import uuid

@api_view(['GET'])
def cake_list_api(request):
    cakes = Cake.objects.all()
    serializer = CakeSerializer(cakes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cake_detail_api(request, id):
    try:
        cake = Cake.objects.get(id=id)
        data = {
            "id": cake.id,
            "name": cake.name,
            "price": cake.price,
            "image": cake.image.url if cake.image else None,
        }
        return JsonResponse(data)
    except Cake.DoesNotExist:
        return JsonResponse({"error": "Cake not found"}, status=404)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.prefetch_related('cakes')
    data = []
    for cat in categories:
        data.append({
            "id": cat.id,
            "name": cat.name,
            "cakes": [
                {
                    "id": cake.id,
                    "name": cake.name,
                    "price": cake.price,
                    "image": request.build_absolute_uri(cake.image.url) if cake.image else "",
                }
                for cake in cat.cakes.all()
            ]
        })

    return Response(data)

@api_view(['GET'])
def branch_list(request):
    branches = Branch.objects.all()
    data = []
    for b in branches:
        data.append({
            "id": b.id,
            "name": b.name,
            "location": b.location,
            "phone": b.phone,
            "map_url": b.map_url,
            "open_time": b.open_time,
            "close_time": b.close_time,
            "is_main": b.is_main,
        })
    return Response(data)

@api_view(['POST'])
def orders_api(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        order = serializer.save() 

        return Response(
            {
                "message": "Order placed successfully",
                "order_no": order.order_no,
                "order_id": order.id,
                "total": order.total,
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def order_detail_api(request, id):
    try:
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def cancel_order(request, pk):
    try:
        order = Order.objects.get(id=pk, user=request.user)
        order.status = "cancelled"
        order.save()
        return Response({"message": "Order cancelled"})
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)
