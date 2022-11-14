from rest_framework import serializers

from .models import Product, Network


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=25)
    product_model = serializers.CharField()
    product_launch_date = serializers.DateField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_model = validated_data.get('product_model', instance.product_model)
        instance.product_launch_date = validated_data.get('product_launch_date', instance.product_launch_date)
        instance.save()
        return instance


class NetworkSerializer(serializers.Serializer):
    type = serializers.CharField()
    name = serializers.CharField(max_length=50)
    email = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    street = serializers.CharField()
    house_number = serializers.CharField()
    employees = serializers.CharField()
    debt = serializers.FloatField()
    products = ProductSerializer(many=True)

    def create(self, validated_data):
        return Network.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.employees = validated_data.get('employees', instance.employees)
        instance.products = validated_data.get('products', instance.products)
        instance.save()
        return instance
