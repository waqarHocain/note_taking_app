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

    def test_redirects_to_note_detail_page_after_creating_note(self):
        response = self.client.post(
            self.url,
            data={"title": "This is heading", "body": "This is content of note"},
        )

        expected_url = reverse("notes:detail", args=[Note.objects.first().id])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, expected_url)


class ListNotesView(TestCase):
    def setUp(self):
        self.url = reverse("notes:list")

    def test_request_resolves_to_200_status_code(self):
        response = self.client.get(self.url)

        assert response.status_code == 200, "Response should be 200 OK"

    def test_renders_correct_template(self):
        template_name = "notes/list_notes.html"

        response = self.client.get(self.url)

        self.assertIn(template_name, [template.name for template in response.templates])

    def test_passes_correct_context_to_template(self):
        Note.objects.create(title="test", body="jfksdj fjdsl")

        response = self.client.get(self.url)

        self.assertIsInstance(response.context["notes"][0], Note)

    def test_notes_are_retrieved_in_descending_order(self):
        # this also tests all objects are passed in context
        n1 = Note.objects.create(title="note 1", body="jfksdj fjdsl")
        n2 = Note.objects.create(title="note 2", body="jfksdj fjdsl")
        n3 = Note.objects.create(title="note 3", body="jfksdj fjdsl")

        response = self.client.get(self.url)

        self.assertEqual(response.context["notes"][0], n3)
        self.assertEqual(response.context["notes"][2], n1)


class DetailNoteView(TestCase):
    def setUp(self):
        self.note = Note.objects.create()
        self.url = reverse("notes:detail", args=[self.note.id])

    def test_request_resolves_to_200_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(self.url)
        template_name = "notes/note_detail.html"
        self.assertIn(template_name, [template.name for template in response.templates])

    def test_passes_correct_context_to_template(self):
        response = self.client.get(self.url, args=[self.note.id])

        self.assertIsInstance(response.context["note"], Note)


class UpdateNoteView(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="My Note", body="My note body text")
        self.url = reverse("notes:update", args=[self.note.id])

    def test_request_resolves_to_200_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(self.url)
        template_name = "notes/add_note.html"
        self.assertIn(template_name, [template.name for template in response.templates])

    def test_passes_correct_context_to_template(self):
        response = self.client.get(self.url, args=[self.note.id])

        self.assertEqual(response.context["update"], True)
        self.assertIsInstance(response.context["note"], Note)


class DeleteNoteView(TestCase):
    def test_deletes_a_note(self):
        n1 = Note.objects.create(title="My Note 1", body="My note body text")
        url = reverse("notes:delete", args=[n1.id])
        response = self.client.post(url, data={})

        self.assertEqual(Note.objects.count(), 0)

    def test_redirects_to_notes_listing_page(self):
        n1 = Note.objects.create(title="My Note 1", body="My note body text")
        url = reverse("notes:delete", args=[n1.id])
        response = self.client.post(url, data={})

        expected_url = reverse("notes:list")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, expected_url)
