from rest_framework import views, status
from rest_framework.response import Response


class ReserveAPIView(views.APIView):
    def get(self, request):
        return Response({'data': 'successfully'}, status=status.HTTP_200_OK)
