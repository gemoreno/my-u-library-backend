from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from library.permissions.roles import IsLibrarian, IsStudent
from rest_framework import status

from ..models import Book, CheckoutRecord
from ..serializers import BooksSerializer, AddedBookSerializer, BookWithCheckoutDateSerializer
from django.db.models import Count, Q, F, ExpressionWrapper, IntegerField

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def books_handler(request):
    if request.method == 'GET':
        title = request.GET.get('title', '').strip()
        author = request.GET.get('author', '').strip()
        genre = request.GET.get('genre', '').strip()

        books = Book.objects.filter(
            title__icontains=title,
            author__icontains=author,
            genre__icontains=genre
        ).annotate(
            available=ExpressionWrapper(
                F('stock') - Count('checkout_records', filter=Q(checkout_records__returned=False)),
                output_field=IntegerField()
            )
        )

        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        permission = IsLibrarian()
        if not permission.has_permission(request, None):
            return Response({'detail': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            addedBook = serializer.save()
            return Response(AddedBookSerializer(addedBook).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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