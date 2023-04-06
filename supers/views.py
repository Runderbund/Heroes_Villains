from django.shortcuts import get_object_or_404
from .models import Super
from rest_framework.decorators import api_view
from .serializers import SuperSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)