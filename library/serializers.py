from rest_framework import serializers
from .models import Book, CheckoutRecord
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
        
        
User = get_user_model()


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role']


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        refresh = self.get_token(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class BookSerializer(serializers.ModelSerializer):
    available = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'year_published', 'stock', 'available']
        

class BookWithCheckoutDateSerializer(serializers.ModelSerializer):
    checkout_date = serializers.DateTimeField(source='date_out')
    title = serializers.CharField(source='book.title', read_only=True)
    genre = serializers.CharField(source='book.genre', read_only=True)
    author = serializers.CharField(source='book.author', read_only=True)
    year_published = serializers.IntegerField(source='book.year_published', read_only=True)
    stock = serializers.IntegerField(source='book.stock', read_only=True)
    available = serializers.IntegerField(read_only=True)

    class Meta:
        model = CheckoutRecord
        fields = ['id', 'title', 'author', 'genre', 'year_published', 'stock', 'available', 'checkout_date']
        
        
class CheckoutRecordSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = CheckoutRecord
        fields = [
            'id', 'user', 'book', 'date_out', 'is_returned', 'date_returned',
            'user_email', 'user_first_name', 'user_last_name', 'book_title'
        ]