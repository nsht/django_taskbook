from django.test import TestCase
from .models import TodoItem,SubItem
from django.utils import timezone
import pdb

class TodoTestCase(TestCase):
    def setUp(self):
        TodoItem.objects.create(
            todo_item="Test",description="description",created=timezone.now(),status=0
        )
        todo = TodoItem.objects.get(todo_item="Test")
        SubItem.objects.create(
            sub_item = "Sub Item",sub_created=timezone.now(),todo_id=todo
        )

    def test_todo_creation(self):
        # Check object creation
        todo = TodoItem.objects.get(todo_item="Test")
        self.assertEqual(todo.todo_item,"Test")
        sub = SubItem.objects.get(sub_item = "Sub Item")
        self.assertEqual(sub.sub_item,"Sub Item")

        # Check fkey references
        self.assertEqual(sub.todo_id_id,todo.id)