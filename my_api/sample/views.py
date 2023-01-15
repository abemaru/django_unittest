from rest_framework.views import APIView
from rest_framework.response import Response

class OnlyViews(APIView):
    
    def get(self, request, format=None):
        return Response(
            ["foo", "bar"]
        )

    def post(self, request, format=None):
        
        return Response(int(request.data.get("number")) + 1)
