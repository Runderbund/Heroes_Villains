from django.shortcuts import get_object_or_404
from .models import Super
from rest_framework.decorators import api_view
from .serializers import SuperSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)

    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST', 'GET'])
def supers_list(request):
    if request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        super_type = request.query_params.get('type')
        super_list = Super.objects.all()

        if super_type:
            super_list = Super.objects.filter(super_type__super_type=super_type) #Not sure here

        serializer = SuperSerializer(super_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# (/10 points) As a developer, I want to create a GET endpoint that responds with a 200 success status code and all of the supers within the supers table. 
# This view function should be implemented in a way to accept a “type” parameter 
# Example: " http://127.0.0.1:8000/api/supers?type=hero” 
# If a type query parameter is sent to the view function with the value of “hero”, the view function response should be a list of all supers that are associated with the type of “Hero” (Shown in End Result Overview video on portal) 
# If a type query parameter is sent to the view function with the value of “villain”, the view function response should be a list of all supers that are associated with the type of “Villain” (Shown in End Result Overview video on portal) 
#  If no type query parameter is sent, return a custom dictionary response with a “heroes” key set equal to a list of supers of type “Hero” and a “villains” key set equal to a list of supers of type “Villain” (Shown in End Result Overview video on portal) 
# custom_response = {“heroes” = [], “villains” = []} 