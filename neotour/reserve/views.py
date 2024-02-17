from rest_framework import views, status
from rest_framework.response import Response

from .serializers import ReserveSerializer
from .models import Reserve


class ReserveAPIView(views.APIView):
    def get(self, request):
        try:
            reserves = Reserve.objects.all()
        except Exception as e:
            return Response({'data': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ReserveSerializer(reserves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
