from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/new_page/', views.new_page, name='new_page'),
    path('details/', views.student_details, name='details'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
    path('details/success/', views.success, name='success'),
    path('logout', views.logout, name='logout'),
]