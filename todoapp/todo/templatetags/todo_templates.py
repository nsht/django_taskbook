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
    elif diff.days >= 1 and diff.days < 2:
        return "Yesterday"
    # Future date possible time traveller or dst messup
    elif diff.days < 0:
        return str(abs(diff.days)) + " days later"
    else:
        return str(diff.days) + " days ago"