from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def router(request):
    routes = [
        'api/',
        'api/students/'
    ]
    return Response(routes)


@api_view(['GET'])
def students(request):
    student = Student.objects.all()
    
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def student(request, id):
    student = Student.objects.get(id=id)

    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def rooms(request):
    room = Room.objects.get(id=id)

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def rooms(request):
    room = Room.objects.all()

    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def room(request, room_number):
    room = Room.objects.get(room_number=room_number)

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)




