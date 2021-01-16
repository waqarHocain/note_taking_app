from django.urls import path

from .views import HomepageView, AddNoteView, ListNotesView

app_name = "notes"
urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("add/", AddNoteView.as_view(), name="add"),
    path("list/", ListNotesView.as_view(), name="list"),
]
