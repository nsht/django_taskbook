import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
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
        self.credentials = {"username": "test", "password": "12test34"}
        self.user = User.objects.create_user(**self.credentials)

        self.client = Client()

        TodoItem.objects.create(
            todo_user=self.user,
            todo_item="Test",
            description="description",
            created=timezone.now(),
            status=0,
        )
        self.todo = TodoItem.objects.get(todo_item="Test", todo_user=self.user)
        self.subitem = SubItem.objects.create(
            sub_item="Sub Item", sub_created=timezone.now(), todo_id=self.todo
        )

    def test_login(self):
        response = self.client.post("/accounts/login/", self.credentials, follow=True)
        self.assertTrue(response.context["user"].is_active)

    def test_index_page(self):
        response = self.client.post("/accounts/login/", self.credentials, follow=True)
        response = self.client.get("/todo/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context["todos"]), 1)
        self.assertEqual(
            response.context["todos"][0].subitem_set.all()[0].todo_id_id,
            response.context["todos"][0].id,
        )

    def test_star_toggle(self):
        # Toggle star on
        response = self.client.post("/accounts/login/", self.credentials, follow=True)
        response = self.client.post("/todo/toggle-star", {"id": self.todo.id})
        self.todo = TodoItem.objects.get(todo_item="Test")
        self.assertEqual(self.todo.starred, 1)
        self.assertEqual(response.status_code, 200)
        # Toggle star off
        response = self.client.post("/todo/toggle-star", {"id": self.todo.id})
        self.todo = TodoItem.objects.get(todo_item="Test")
        self.assertEqual(self.todo.starred, 0)
        self.assertEqual(response.status_code, 200)

    def test_completion(self):
        # Check sub item
        response = self.client.post("/accounts/login/", self.credentials, follow=True)
        print(response)
        subitem_id = response.context["todos"][0].subitem_set.all()[0].id
        response = self.client.post(
            "/todo/toggle-completion", {"id": subitem_id, "type": "subitem"}
        )
        self.subitem = SubItem.objects.get(id=subitem_id)
        self.assertEqual(self.subitem.status, 1)

        # Uncheck sub item
        response = self.client.post(
            "/todo/toggle-completion", {"id": subitem_id, "type": "subitem"}
        )
        self.subitem = SubItem.objects.get(id=subitem_id)
        self.assertEqual(self.subitem.status, 0)
