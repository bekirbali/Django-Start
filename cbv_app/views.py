from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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
        

class Student_list_crud(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'message':'data deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class Student_GPUD(APIView):
    def get(self,request, pk=0):
        if pk:
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
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
    
        
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'message':'data deleted'}, status=status.HTTP_204_NO_CONTENT)