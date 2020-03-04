import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class AmioAchiAPIView(APIView):
    def post(self, request):
        data = request.data
        x, y = data.pop('x', 0), data.pop('y', 0)
        return Response({'success': False, 'value' : x + y}, status=200)

