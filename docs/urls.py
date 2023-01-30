from django.urls import path, include

from docs import views

urlpatterns = [
    path("register/", views.DocView.as_view()),
]
