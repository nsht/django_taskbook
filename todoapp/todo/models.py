from django.db import models

# Create your models here.


class TodoItem(models.Model):
    status = (
        (0, 'Incomplete'),
        (1, 'Complete')
    )
    starred_choice = (
        (0, 'Unstarred'),
        (1, 'Starred')
    )
    todo_item = models.CharField(max_length=255)
    status = models.IntegerField(choices=status, default=0)
    created = models.DateTimeField("Created")
    updated = models.DateTimeField("Updated", null=True, blank=True)
    description = models.CharField(
        "Description", max_length=255, null=True, blank=True)
    starred = models.IntegerField(
        choices=starred_choice, null=True, default=0, blank=True)
    deadline = models.DateTimeField("Deadline", null=True, blank=True)

    def __str__(self):
        return self.todo_item


class SubItem(models.Model):
    status = (
        (0, 'Incomplete'),
        (1, 'Complete')
    )
    todo_id = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    sub_item = models.CharField(max_length=255)
    status = models.IntegerField(choices=status, default=0)
    sub_created = models.DateTimeField("Created")
    sub_updated = models.DateTimeField("Updated", null=True, blank=True)
    sub_deadline = models.DateTimeField("Deadline", null=True, blank=True)
    sub_description = models.CharField(
        "Description", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.sub_item
