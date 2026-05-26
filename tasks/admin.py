from django.contrib import admin
from .models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "is_done", "deadline", "created_at")
    list_filter = ("is_done", "tags")
    search_fields = ("content",)
    filter_horizontal = ("tags",)
