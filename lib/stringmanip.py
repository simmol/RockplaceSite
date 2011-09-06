__author__="selene"
__date__ ="$Sep 6, 2011 4:25:15 PM$"

from django import template
register = template.Library()

@register.filter
def truncate(value, arg):
    """
    Truncates a string after a given number of chars  
    Argument: Number of chars to truncate after
    """
    try:
        length = int(arg)
    except ValueError: # invalid literal for int()
        return value # Fail silently.
    if not isinstance(value, basestring):
        value = str(value)
    if (len(value) > length):
        return value[:length] + "..."
    else:
        return value

