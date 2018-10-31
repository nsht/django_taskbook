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
    elif (now - datetime.timedelta(1)).day == date.day:
        return "Yesterday"
    # Future date possible time traveller or dst messup
    elif diff.days < 0:
        return str(abs(diff.days)) + " days later"
    else:
        if diff.days == 0:
            pdb.set_trace()
        return str(diff.days) + " days ago"