from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class TaskToggleTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(content="Toggle me")
        self.url = reverse("tasks:task-toggle", kwargs={"pk": self.task.pk})

    def test_toggle_false_to_true(self):
        self.client.post(self.url)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

    def test_toggle_true_to_false(self):
        self.task.is_done = True
        self.task.save()
        self.client.post(self.url)
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_done)

    def test_toggle_redirects_to_home(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse("tasks:task-list"))
