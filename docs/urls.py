from django.urls import path, include

from docs import views

urlpatterns = [
    path("docs/", views.DocView.as_view()),
    path("docs/list/", views.DocListView.as_view()),
]
