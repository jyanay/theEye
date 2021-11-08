from django.urls import path
from theEye import views

urlpatterns = [
    path('create/', views.PostEvent.as_view()),
]