from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializers import StudentSerializer

from rest_framework import status
from rest_framework.generics import get_object_or_404

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



@api_view()
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data) # instance yazsamda oluyor yazmasamda
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'saved successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message':'bad request', 'data':serializer.data}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view()
def student_delete(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response({'message':'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all() 
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    else:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'saved successfully'}, status=status.HTTP_201_CREATED)
        else:
        
            return Response({'message':'bad request'}, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def student_get_put_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    match request.method:
        case 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        case 'PUT':
            serializer = StudentSerializer(instance=student, data=request.data) # instance yazsamda oluyor yazmasamda
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'saved successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':'bad request', 'data':serializer.data}, status=status.HTTP_400_BAD_REQUEST)
        case 'DELETE':
            student.delete()
            return Response({'message':'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)