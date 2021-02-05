from django.test import TestCase

from ..models import Note


class TestModels(TestCase):
    def test_note_has_a_title_and_body(self):
        note = Note.objects.create(title="Reminders", body="Visit a dentist")

        assert Note.objects.count() == 1, "Should be saved in database"
        assert note.title == "Reminders", "Should have a title"
        assert note.body == "Visit a dentist", "Should have a body"

    def test_note_returns_title_when_stringified(self):
        note = Note.objects.create(title="Reminders", body="Visit a dentist")

        assert str(note) == "Reminders", "Should return title"

    def test_note_has_a_correct_absolute_url(self):
        note1 = Note.objects.create(title="Reminders", body="Visit a dentist")
        note2 = Note.objects.create(title="Reminders", body="Visit a dentist")

        expected_url1 = "/notes/1/"
        expected_url2 = "/notes/2/"

        self.assertEqual(note1.get_absolute_url(), expected_url1)
        self.assertEqual(note2.get_absolute_url(), expected_url2)
