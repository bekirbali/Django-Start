from django.urls import path

from .views import (
    Student_list
)

urlpatterns = [
    path('student_list/', Student_list.as_view())
]
