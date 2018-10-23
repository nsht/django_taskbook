from django.contrib import admin
from .models import TodoItem,SubItem
# Register your models here.




class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('todo_item','status','created','description')
    list_filter = ('status','created')


admin.site.register(TodoItem,TodoItemAdmin)
admin.site.register(SubItem)


