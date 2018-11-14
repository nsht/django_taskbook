import unittest
from django.test import TestCase, Client
from .models import TodoItem, SubItem
from django.utils import timezone
import pdb


class TodoTestCase(TestCase):
    def setUp(self):
        TodoItem.objects.create(
            todo_item="Test", description="description", created=timezone.now(), status=0
        )
        todo = TodoItem.objects.get(todo_item="Test")
        SubItem.objects.create(sub_item="Sub Item", sub_created=timezone.now(), todo_id=todo)

    def test_todo_creation(self):
        # Check object creation
        todo = TodoItem.objects.get(todo_item="Test")
        self.assertEqual(todo.todo_item, "Test")
        sub = SubItem.objects.get(sub_item="Sub Item")
        self.assertEqual(sub.sub_item, "Sub Item")

        # Check fkey references
        self.assertEqual(sub.todo_id_id, todo.id)

        # Check __str__ functions
        self.assertEqual(todo.__str__(), todo.todo_item)
        self.assertEqual(sub.__str__(), sub.sub_item)


# TODO read up on setUpClass
class SimpleTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.client = Client()

        TodoItem.objects.create(
            todo_item="Test", description="description", created=timezone.now(), status=0
        )
        self.todo = TodoItem.objects.get(todo_item="Test")
        SubItem.objects.create(sub_item="Sub Item", sub_created=timezone.now(), todo_id=self.todo)

    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context["todos"]), 1)
        self.assertEqual(
            response.context["todos"][0].subitem_set.all()[0].todo_id_id,
            response.context["todos"][0].id,
        )

    def test_star_toggle(self):
        # Toggle star on
        response = self.client.post("/toggle-star", {"id": self.todo.id})
        self.todo = TodoItem.objects.get(todo_item="Test")
        self.assertEqual(self.todo.starred, 1)
        self.assertEqual(response.status_code, 200)
        # Toggle star off
        response = self.client.post("/toggle-star", {"id": self.todo.id})
        self.todo = TodoItem.objects.get(todo_item="Test")
        self.assertEqual(self.todo.starred, 0)
        self.assertEqual(response.status_code, 200)
