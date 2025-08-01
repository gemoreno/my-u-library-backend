from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from library.permissions.roles import IsLibrarian
from ..models import Book, CheckoutRecord
from ..serializers import CheckoutSerializer
from library.permissions.roles import IsStudent

@api_view(['POST'])
@permission_classes([IsStudent])
def checkout_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.stock <= 0:
        return Response({"error": "No copies available."}, status=400)
    
    CheckoutRecord.objects.create(user=request.user, book=book)
    return Response({"message": "Book checked out successfully."})

@api_view(['GET'])
@permission_classes([IsLibrarian])
def list_checkouts(request):
    if not request.user.role == 'librarian':
        return Response({'error': 'Only librarians can access this.'}, status=403)

    first_name = request.GET.get('first_name', '').strip()
    last_name = request.GET.get('last_name', '').strip()
    email = request.GET.get('email', '').strip()
    title = request.GET.get('title', '').strip()

    checkouts = CheckoutRecord.objects.select_related('user', 'book').filter(
        user__first_name__icontains=first_name,
        user__last_name__icontains=last_name,
        user__email__icontains=email,
        book__title__icontains=title,
        is_returned=False
    )

    serializer = CheckoutSerializer(checkouts, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsLibrarian])
def return_book(request, checkout_id):
    if not request.user.role == 'librarian':
        return Response({'error': 'Only librarians can return books.'}, status=403)

    checkout = get_object_or_404(CheckoutRecord, id=checkout_id)
    
    if checkout.is_returned:
        return Response({'message': 'Book already returned.'}, status=400)
    
    checkout.is_returned = True
    checkout.date_returned = timezone.now()
    checkout.save()

    return Response({'message': 'Book returned successfully.'})