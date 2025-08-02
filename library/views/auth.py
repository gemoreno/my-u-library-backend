from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status

from library.permissions.roles import IsAdminOrLibrarian
from library.serializers import EmailTokenObtainPairSerializer, UserSerializer, UserRegistrationSerializer

@permission_classes([AllowAny])
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


@api_view(['GET'])
def me_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminOrLibrarian])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserRegistrationSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)