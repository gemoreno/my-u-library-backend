from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from library.serializers import EmailTokenObtainPairSerializer, MeSerializer

@permission_classes([AllowAny])
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


@api_view(['GET'])
def me_view(request):
    serializer = MeSerializer(request.user)
    return Response(serializer.data)