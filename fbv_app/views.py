from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import Response

# Create your views here.


def home(request):
    return Response(
        {
            "hello world this is new thing"
        }
    )