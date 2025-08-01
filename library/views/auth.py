from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from library.serializers import EmailTokenObtainPairSerializer

@permission_classes([AllowAny])
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
