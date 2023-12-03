from rest_framework import serializers
from .models import StockPrice


class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ["symbol", "quantity","current_price", "datetime"]
