from django.urls import path

from .views import (
    Student_list,
    Student_list_crud,
    Student_GPUD
)

urlpatterns = [
    path('student_list/', Student_list.as_view()),
    path('student_list_crud/<str:pk>', Student_list_crud.as_view()),
    path('student_gpud/<str:pk>', Student_GPUD.as_view()),
    path('student_gpud/', Student_GPUD.as_view()),
]
