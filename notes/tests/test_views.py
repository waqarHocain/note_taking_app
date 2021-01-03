from django.test import TestCase
from django.urls import reverse


class HomepageViewTest(TestCase):
    def test_request_to_homepage_url_returns_200_status_code(self):
        url = reverse("homepage")
        response = self.client.get(url)

        assert response.status_code == 200, "Response should be 200 OK"

    def test_homepage_view_renders_correct_template(self):
        template_name = "notes/home.html"
        url = reverse("homepage")
        response = self.client.get(url)

        self.assertIn(template_name, [template.name for template in response.templates])
