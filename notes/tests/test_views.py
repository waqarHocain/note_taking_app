from django.test import TestCase
from django.urls import reverse

from notes.models import Note
from notes.forms import NoteForm


class HomepageViewTest(TestCase):
    def test_request_to_homepage_url_returns_200_status_code(self):
        url = reverse("notes:homepage")
        response = self.client.get(url)

        assert response.status_code == 200, "Response should be 200 OK"

    def test_homepage_view_renders_correct_template(self):
        template_name = "notes/home.html"
        url = reverse("notes:homepage")
        response = self.client.get(url)

        self.assertIn(template_name, [template.name for template in response.templates])


class AddNoteViewTest(TestCase):
    def setUp(self):
        self.url = reverse("notes:add")

    def test_request_resolves_to_200_status_code(self):
        response = self.client.get(self.url)

        assert response.status_code == 200, "Response should be 200 OK"

    def test_renders_correct_template(self):
        template_name = "notes/add_note.html"
        response = self.client.get(self.url)

        self.assertIn(template_name, [template.name for template in response.templates])

    def test_form_is_passed_in_context(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.context["form"], NoteForm)

    def test_post_request_create_a_note_object_in_database(self):
        response = self.client.post(
            self.url,
            data={"title": "This is heading", "body": "This is content of note"},
        )

        saved_note = Note.objects.first()

        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(saved_note.title, "This is heading")
