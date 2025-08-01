from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from library.permissions.roles import IsStudent

from ..models import Book, CheckoutRecord
from ..serializers import BookSerializer, BookWithCheckoutDateSerializer
from django.db.models import Count, Q, F, ExpressionWrapper, IntegerField

@api_view(['GET'])
@permission_classes([AllowAny])
def filtered_books(request):
    title = request.GET.get('title', '').strip()
    author = request.GET.get('author', '').strip()
    genre = request.GET.get('genre', '').strip()

    books = Book.objects.filter(
        title__icontains=title,
        author__icontains=author,
        genre__icontains=genre
    ).annotate(
        available=ExpressionWrapper(
            F('stock') - Count('checkout_records', filter=Q(checkout_records__is_returned=False)),
            output_field=IntegerField()
        )
    )

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsStudent])
def filtered_checked_books(request):
    title = request.GET.get('title', '').strip()
    author = request.GET.get('author', '').strip()
    genre = request.GET.get('genre', '').strip()

    checkouts = CheckoutRecord.objects.select_related('book').filter(
        user=request.user,
        returned=False,
        book__title__icontains=title,
        book__author__icontains=author,
        book__genre__icontains=genre
    )
    
    serializer = BookWithCheckoutDateSerializer(checkouts, many=True)
    return Response(serializer.data)