from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Tag, Task

class TagModelTest(TestCase):

    def test_tag_str_returns_name(self):
        tag = Tag.objects.create(name="urgent")
        self.assertEqual(str(tag), "urgent")

    def test_tag_ordering_is_alphabetical(self):
        Tag.objects.create(name="work")
        Tag.objects.create(name="home")
        Tag.objects.create(name="finance")
        names = list(Tag.objects.values_list("name", flat=True))
        self.assertEqual(names, sorted(names))


class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(content="Buy milk")

    def test_task_defaults_to_not_done(self):
        self.assertFalse(self.task.is_done)

    def test_task_deadline_is_optional(self):
        self.assertIsNone(self.task.deadline)

    def test_task_deadline_can_be_set(self):
        deadline = timezone.now() + timezone.timedelta(days=3)
        self.task.deadline = deadline
        self.task.save()
        self.task.refresh_from_db()
        self.assertIsNotNone(self.task.deadline)

    def test_task_str_shows_pending_indicator(self):
        self.assertIn("○", str(self.task))

    def test_task_str_shows_done_indicator(self):
        self.task.is_done = True
        self.task.save()
        self.assertIn("✓", str(self.task))

    def test_task_can_have_multiple_tags(self):
        tag1 = Tag.objects.create(name="personal")
        tag2 = Tag.objects.create(name="shopping")
        self.task.tags.add(tag1, tag2)
        self.assertEqual(self.task.tags.count(), 2)
