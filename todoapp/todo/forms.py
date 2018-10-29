from django import forms
from .models import TodoItem, SubItem


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('todo_item',)
