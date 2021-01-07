from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import NoteForm


class HomepageView(TemplateView):
    template_name = "notes/home.html"


class AddNoteView(CreateView):
    form_class = NoteForm
    template_name = "notes/add_note.html"
    success_url = reverse_lazy("notes:add")
