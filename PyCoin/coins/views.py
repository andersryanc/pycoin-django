from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Coin
from .serializers import CoinSerializer


# List all coins or creates a new one
# coins/
class CoinList(APIView):

    def get(self, request):
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
