from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import NoteForm
from .models import Note


class HomepageView(TemplateView):
    template_name = "notes/home.html"


class AddNoteView(CreateView):
    form_class = NoteForm
    template_name = "notes/add_note.html"


class ListNotesView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/list_notes.html"


class DetailNoteView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"


class UpdateNoteView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/add_note.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update"] = True
        return context
