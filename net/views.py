from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import ProductSerializer, NetworkSerializer
from .models import Product, Network
from django_filters import rest_framework as filters
from .permissions import ActiveUserPermission


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [ActiveUserPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        product = request.data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.product_name)})

    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('products')
        serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({
            "success": "Product '{}' updated successfully".format(product_saved.product_name)
        })

    def delete(self, request, pk):
        article = get_object_or_404(Product.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Product with id `{}` has been deleted.".format(pk)
        }, status=204)


class NetworkFilter(filters.FilterSet):
    avg_debt = filters.NumberFilter(field_name="debt", lookup_expr='gt')

    class Meta:
        model = Network
        fields = ['country', 'products']


class NetworkViewSet(viewsets.ModelViewSet):
    permission_classes = [ActiveUserPermission]
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filterset_class = NetworkFilter

    def delete(self, request, pk):
        network_element = get_object_or_404(Network.objects.all(), pk=pk)
        network_element.delete()
        return Response({
            "message": "Network_element with id `{}` has been deleted.".format(pk)
        }, status=204)
