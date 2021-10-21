from rest_framework import serializers
from .models import Shoes, Brand



class ShoesSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.HyperlinkedRelatedField(
        view_name='shoes_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Shoes
        fields = ('id', 'type', 'brand_name', 'brand_url', 'brand')

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.HyperlinkedRelatedField(
        view_name='brand_detail',
        many = False,
        read_only=True
    )
    class Meta:
        model = Brand
        fields = ('id', 'name', 'type', 'brand_url')

