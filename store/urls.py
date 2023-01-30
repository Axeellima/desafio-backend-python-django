from django.urls import path, include

from store import views

urlpatterns = [
    path("store/", views.StoreView.as_view()),
]
