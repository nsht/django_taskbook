import datetime

from django.utils import timezone
from django import template
import pdb
register = template.Library()

@register.filter(expects_localtime=True)
def custom_timestamp(date):
    now = timezone.localtime(timezone.now())
    diff = now - date
    if now.day == date.day:
        return "Today"
    elif now.day - date.day == 1:
        return "Yesterday"
    elif diff.days < 0:
        return str(abs(diff.days)) + " days later"
    else:
        return str(diff.days) + " days ago"