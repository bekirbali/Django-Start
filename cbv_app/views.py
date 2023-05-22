from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

def home(request):
    pass

class Student_list(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)