from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Tag, Task


class TaskSortingTest(TestCase):

    def test_undone_tasks_appear_before_done(self):
        Task.objects.create(content="Done task", is_done=True)
        Task.objects.create(content="Pending task", is_done=False)
        response = self.client.get(reverse("tasks:task-list"))
        tasks = list(response.context["task_list"])
        done_flags = [t.is_done for t in tasks]
        self.assertEqual(done_flags, sorted(done_flags))

    def test_newer_tasks_appear_before_older_within_same_status(self):
        old = Task.objects.create(content="Old task")
        new = Task.objects.create(content="New task")
        response = self.client.get(reverse("tasks:task-list"))
        tasks = list(response.context["task_list"])
        ids = [t.pk for t in tasks]
        self.assertLess(ids.index(new.pk), ids.index(old.pk))