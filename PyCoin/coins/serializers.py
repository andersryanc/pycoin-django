from rest_framework import serializers
from .models import Coin


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        # NOTE: only some fields?
        # fields = ('description')
        fields = '__all__'
