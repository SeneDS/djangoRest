from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ("id", "name", "price", "content", "my_discount", "get_discount")

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount


    def validate_price(self, value):
        # Vérifie que ce n'est pas un nombre complexe
        if isinstance(value, complex):
            raise serializers.ValidationError("Ce champ ne prend pas de nombre complexe.")
        return value
