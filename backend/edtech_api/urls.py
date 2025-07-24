from django.urls import path
from . import views

urlpatterns = [
    path('assignments/create/', views.create_assignment),
    path('assignments/submit/<int:id>/', views.submit_assignment),
    path('submissions/<int:assignment_id>/', views.view_submissions),
]
