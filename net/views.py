from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import ProductSerializer, NetworkSerializer
from .models import Product, Network


class ProductViewSet(viewsets.ModelViewSet):
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


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    def post(self, request):
        network_elements = request.data
        serializer = ProductSerializer(data=network_elements)
        if serializer.is_valid(raise_exception=True):
            network_elements_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(network_elements_saved.product_name)})

    def put(self, request, pk):
        saved_network_element = get_object_or_404(Network.objects.all(), pk=pk)
        data = request.data.get('networks')
        serializer = NetworkSerializer(instance=saved_network_element, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            network_element_saved = serializer.save()
        return Response({
            "success": "Network_element '{}' updated successfully".format(network_element_saved.product_name)
        })
    #
    # def delete(self, request, pk):
    #     article = get_object_or_404(Product.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({
    #         "message": "Product with id `{}` has been deleted.".format(pk)
    #     }, status=204)