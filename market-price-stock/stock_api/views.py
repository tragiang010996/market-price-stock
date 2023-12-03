from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .repositories import StockPriceRepository
from .serializers import StockPriceSerializer
from logging import Logger

logger = Logger(__name__)

class StockAPIView(APIView):
    def get(self, request, *args, **kwargs):
        symbol: str = request.query_params.get("symbol")
        quantity: str = request.query_params.get("quantity")

        if not symbol or not isinstance(symbol, str):
            return Response(
                {"message": "Symbol not found."}, status=status.HTTP_400_BAD_REQUEST
            )

        if not quantity or not quantity.isdigit() or int(quantity) <= 0:
            return Response(
                {"message": "Quantity invalid."}, status=status.HTTP_400_BAD_REQUEST
            )

        stock_price_repo = StockPriceRepository()
        response = stock_price_repo.get_current_stock_price(symbol, quantity)
        if not response["status"]:
            return Response(
                {"message": response["reason"]},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        stock_price = response["stock_price"]
        stock_price_serializer = StockPriceSerializer(data=stock_price)
        if not stock_price_serializer.is_valid():
            return Response(
                stock_price_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        
        stock_price_model = stock_price_serializer.save()
        stock_price_model.save()
        return Response(stock_price_serializer.data, status=status.HTTP_200_OK)
