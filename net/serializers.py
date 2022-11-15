from rest_framework import serializers

from .models import Product, Network


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
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
    parent = serializers.PrimaryKeyRelatedField(queryset=Network.objects.all(), allow_null=True)
    email = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    street = serializers.CharField()
    house_number = serializers.CharField()
    employees = serializers.CharField()
    debt = serializers.FloatField()
    pub_date = serializers.DateTimeField()
    products = ProductSerializer(many=True)

    def get_or_create_products(self, products):
        products_ids = []
        for product in products:
            products_instance, created = Product.objects.get_or_create(pk=product.get('id'), defaults=product)
            products_ids.append(products_instance.pk)
        return products_ids

    def create_or_update_products(self, products):
        products_ids = []
        for product in products:
            products_instance, created = Product.objects.update_or_create(pk=product.get('id'), defaults=product)
            products_ids.append(products_instance.pk)
        return products_ids

    def create(self, validated_data):
        product = validated_data.pop('products', [])
        network = Network.objects.create(**validated_data)
        network.products.set(self.get_or_create_products(product))
        return network

    def update(self, instance, validated_data):
        product = validated_data.pop('products', [])
        instance.products.set(self.create_or_update_products(product))
        fields = [
            'type', 'name', 'parent', 'email', 'country', 'city',
            'street', 'house_number', 'employees', 'debt', 'pub_date', 'products'
        ]
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance

    def validate_debt(self, value):
        if self.instance and value != self.instance.debt:
            raise serializers.ValidationError("Change of debt is prohibited.")
        return value
