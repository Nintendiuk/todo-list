from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Tag, Task


class TaskViewAccessibilityTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(content="Sample task")

    def test_home_page_returns_200(self):
        response = self.client.get(reverse("tasks:task-list"))
        self.assertEqual(response.status_code, 200)

    def test_task_create_returns_200(self):
        response = self.client.get(reverse("tasks:task-create"))
        self.assertEqual(response.status_code, 200)

    def test_task_update_returns_200(self):
        response = self.client.get(
            reverse("tasks:task-update", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_task_delete_returns_200(self):
        response = self.client.get(
            reverse("tasks:task-delete", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_task_create_post_redirects_to_home(self):
        response = self.client.post(
            reverse("tasks:task-create"), {"content": "New task", "tags": []}
        )
        self.assertRedirects(response, reverse("tasks:task-list"))

    def test_task_delete_post_redirects_to_home(self):
        response = self.client.post(
            reverse("tasks:task-delete", kwargs={"pk": self.task.pk})
        )
        self.assertRedirects(response, reverse("tasks:task-list"))

    def test_task_delete_removes_from_db(self):
        pk = self.task.pk
        self.client.post(reverse("tasks:task-delete", kwargs={"pk": pk}))
        self.assertFalse(Task.objects.filter(pk=pk).exists())


class TagViewAccessibilityTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="test-tag")

    def test_tag_list_returns_200(self):
        response = self.client.get(reverse("tasks:tag-list"))
        self.assertEqual(response.status_code, 200)

    def test_tag_create_returns_200(self):
        response = self.client.get(reverse("tasks:tag-create"))
        self.assertEqual(response.status_code, 200)

    def test_tag_update_returns_200(self):
        response = self.client.get(
            reverse("tasks:tag-update", kwargs={"pk": self.tag.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_tag_delete_returns_200(self):
        response = self.client.get(
            reverse("tasks:tag-delete", kwargs={"pk": self.tag.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_tag_create_post_redirects(self):
        response = self.client.post(
            reverse("tasks:tag-create"), {"name": "new-tag"}
        )
        self.assertRedirects(response, reverse("tasks:tag-list"))

    def test_tag_delete_removes_from_db(self):
        pk = self.tag.pk
        self.client.post(reverse("tasks:tag-delete", kwargs={"pk": pk}))
        self.assertFalse(Tag.objects.filter(pk=pk).exists())
