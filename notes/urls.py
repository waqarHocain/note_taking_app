from django.urls import path

from .views import (
    HomepageView,
    AddNoteView,
    ListNotesView,
    DetailNoteView,
    UpdateNoteView,
    DeleteNoteView,
)

app_name = "notes"
urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("add/", AddNoteView.as_view(), name="add"),
    path("notes/", ListNotesView.as_view(), name="list"),
    path("notes/<int:pk>/", DetailNoteView.as_view(), name="detail"),
    path("notes/update/<int:pk>/", UpdateNoteView.as_view(), name="update"),
    path("notes/delete/<int:pk>/", DeleteNoteView.as_view(), name="delete"),
]
