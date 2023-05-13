from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer

# Handles hero/villain list and create operations
@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        # Allows filtering by 'type' parameter in the URL
        if 'type' in request.GET:
            supers = Super.objects.filter(super_type__type=request.GET['type'].capitalize())
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data) #returns serialized data/200 status code
        else:
             # Creates two separate lists of Heroes/Villains if no type is specified
            heroes = Super.objects.filter(super_type__type="Hero")
            villains = Super.objects.filter(super_type__type="Villain")
            serializer_heroes = SuperSerializer(heroes, many=True)
            serializer_villains = SuperSerializer(villains, many=True)
            return Response({"Heroes": serializer_heroes.data, "Villains": serializer_villains.data})

    elif request.method == 'POST':
        # Handles creation of a new Super entry
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handles retrieve, update, and delete operations on individual Supers
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)

    # Retrieves a specific Super entry by id
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Updates a specific Super entry by id
        serializer = SuperSerializer(super, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deletes a specific Super entry by id
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)