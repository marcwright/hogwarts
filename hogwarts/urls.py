from django.urls import path
from . import views

urlpatterns = [
    path('', views.house_list),
    path('houses/', views.house_list, name = 'house_list'),
    path('houses/<int:id>', views.house_detail, name = 'house_detail'),
    path('houses/new', views.house_create, name = 'house_create'),
    path('houses/<int:id>/edit', views.house_update, name = 'house_update'),
    path('houses/<int:id>/delete', views.house_delete, name = 'house_delete'),
    path('students/', views.student_list, name = 'student_list'),
    path('students/<int:id>', views.student_detail, name = 'student_detail'),
    path('students/new', views.student_create, name = 'student_create'),
    path('students/<int:id>/edit', views.student_update, name = 'student_edit'),
    path('students/<int:id>/delete', views.student_delete, name = 'student_delete'),
]
