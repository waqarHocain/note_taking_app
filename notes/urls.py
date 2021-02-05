from django.urls import path

from .views import HomepageView, AddNoteView, ListNotesView, DetailNoteView

app_name = "notes"
urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("add/", AddNoteView.as_view(), name="add"),
    path("notes/", ListNotesView.as_view(), name="list"),
    path("notes/<int:pk>/", DetailNoteView.as_view(), name="detail"),
]
