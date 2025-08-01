from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from library.permissions.roles import IsLibrarian
from ..models import CheckoutRecord
from ..serializers import CheckoutSerializer

@api_view(['GET'])
@permission_classes([IsLibrarian])  # optionally add IsLibrarian custom permission
def list_checkouts(request):
    if not request.user.role == 'librarian':
        return Response({'error': 'Only librarians can access this.'}, status=403)

    first_name = request.GET.get('first_name', '').strip()
    last_name = request.GET.get('last_name', '').strip()
    email = request.GET.get('email', '').strip()
    title = request.GET.get('title', '').strip()

    checkouts = CheckoutRecord.objects.select_related('student', 'book').filter(
        student__first_name__icontains=first_name,
        student__last_name__icontains=last_name,
        student__email__icontains=email,
        book__title__icontains=title,
    )

    serializer = CheckoutSerializer(checkouts, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsLibrarian])  # optionally use IsLibrarian
def return_book(request, checkout_id):
    if not request.user.role == 'librarian':
        return Response({'error': 'Only librarians can return books.'}, status=403)

    checkout = get_object_or_404(CheckoutRecord, id=checkout_id)
    
    if checkout.is_returned:
        return Response({'message': 'Book already returned.'}, status=400)
    
    checkout.is_returned = True
    checkout.save()

    return Response({'message': 'Book returned successfully.'})