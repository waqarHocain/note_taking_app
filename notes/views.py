from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import NoteForm
from .models import Note


class HomepageView(TemplateView):
    template_name = "notes/home.html"


class AddNoteView(CreateView):
    form_class = NoteForm
    template_name = "notes/add_note.html"
    success_url = reverse_lazy("notes:add")


class ListNotesView(TemplateView):
    template_name = "notes/list_notes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = Note.objects.all()
        return context
