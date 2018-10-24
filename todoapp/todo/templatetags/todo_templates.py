import datetime

from django.utils import timezone
from django import template

register = template.Library()

@register.filter
def custom_timestamp(date):
    now = timezone.now()
    diff = now - date
    if diff < datetime.timedelta(1):
        return "Today"
    elif diff < datetime.timedelta(2) and diff > datetime.timedelta(1):
        return "Yesterday"
    else:
        return str(diff.days) + " days ago"