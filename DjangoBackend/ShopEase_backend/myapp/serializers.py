from rest_framework import serializers
from .models import *

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)  
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        source='category',  
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'category_id', 'description',
            'price', 'created_at', 'updated_at', 'image', 'slug'
        ]

class DetailedProductSerializer(serializers.ModelSerializer):
    similar_products = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "name", "price", "slug", "image", "description", "similar_products"]

    def get_similar_products(self, product):
        products = Product.objects.filter(category_id=product.category_id).exclude(id=product.id)
        serializer = ProductSerializer(products, many=True)
        return serializer.data
    

class HomePageProductSerializer(serializers.ModelSerializer):
    home_page_products = serializers.SerializerMethodField()
    class Meta:
        model = Product
        [
            'id', 'name', 'category', 'category_id', 'description',
            'price', 'created_at', 'updated_at', 'image', 'home_page_products', 'slug'
        ]


    def get_home_page_products(self, product):
        products = Product.objects.filter(category_id=product.category_id).exclude(id=product.id).order_by('?')[:12]
        serializer = ProductSerializer(products, many=True)
        return serializer.data
    

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem 
        fields = ["id", "quantity", "product", "total"]


    def get_total(self, cartitem):
        price = cartitem.product.price * cartitem.quantity
        return price
    

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)
    sum_total = serializers.SerializerMethodField()
    num_of_items = serializers.SerializerMethodField()
    num_of_product = serializers.SerializerMethodField()
    class Meta:
        model = Cart 
        fields = ["id", "cart_code", "items", "sum_total", "num_of_product", "num_of_items", "created_at", "modified_at"]

    def get_sum_total(self, cart):
        items = cart.items.all()
        total = sum([item.product.price * item.quantity for item in items])
        return total

    def get_num_of_items(self, cart):
        items = cart.items.all()
        total = sum([item.quantity for item in items])
        return total

    def get_num_of_product(self, cart):
        product_ids = CartItem.objects.filter(cart=cart).values_list("product_id", flat=True)
        product_count = product_ids.distinct().count()
        return product_count


class SimpleCartSerializer(serializers.ModelSerializer):
    num_of_items = serializers.SerializerMethodField()
    class Meta:
        model = Cart 
        fields = ["id", "cart_code", "num_of_items"]

    def get_num_of_items(self, cart):
        num_of_items = sum([item.quantity for item in cart.items.all()])
        return num_of_items


class NewCartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order_id = serializers.SerializerMethodField()
    order_date = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "order_id", "order_date"]

    def get_order_id(self, cartitem):
        order_id = cartitem.cart.cart_code
        return order_id
    
    def get_order_date(self, cartitem):
        order_date = cartitem.cart.modified_at
        return order_date