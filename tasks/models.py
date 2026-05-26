from django.db import models


class Tag(models.Model):
    """A label that can be attached to multiple tasks."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    """A single to-do item with optional deadline and tags."""

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created_at"]

    def __str__(self):
        status = "✓" if self.is_done else "○"
        return f"[{status}] {self.content[:50]}"

