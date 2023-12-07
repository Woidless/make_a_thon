from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
# 
from rest_framework import permissions
# 

class DataTruckView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.DataTruckSerializers(data=request.data)
        return Response('Bad request!', status=400)