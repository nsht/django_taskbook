from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('',views.index,name='index'),
    path('new',views.new_todo,name='new_todo'),
    path('add',views.add_todo,name='add_todo'),
    path('toggle-completion',views.toggle_completion,name='toggle_completion')
]