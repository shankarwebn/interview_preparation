# shop/serializers.py

from rest_framework import serializers
from .models import User, Product, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'address', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')   # password अलग करो
        user = User(**validated_data)               # user create (without password)
        user.set_password(password)                 # 🔐 hashing
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product'
    )

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'product_id']