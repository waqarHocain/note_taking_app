from django.test import TestCase

from notes.forms import NoteForm


class NoteFormTest(TestCase):
    def test_form_title_and_body_has_placeholder(self):
        form = NoteForm()
        self.assertIn('placeholder="Enter note title"', form.as_p())
        self.assertIn('placeholder="Enter note content"', form.as_p())
