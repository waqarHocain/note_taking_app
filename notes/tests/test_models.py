from django.test import TestCase

from ..models import Note


class TestModels(TestCase):
    def test_note_has_a_title_and_body(self):
        note = Note.objects.create(title="Reminders", body="Visit a dentist")

        assert Note.objects.count() == 1, "Should be saved in database"
        assert note.title == "Reminders", "Should have a title"
        assert note.body == "Visit a dentist", "Should have a body"
