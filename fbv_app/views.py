from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializers import StudentSerializer

from rest_framework import status

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response(
        {
           'message': 'hello world this is new thing'
        }
    )

@api_view()
def student_list(request):
    students = Student.objects.all() 
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'saved successfully'}, status=status.HTTP_201_CREATED)
    else:
        
        return Response({'message':'bad request'}, status=status.HTTP_400_BAD_REQUEST)
