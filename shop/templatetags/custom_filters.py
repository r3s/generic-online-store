from django import template
register = template.Library()

@register.filter
def get_attr(obj, atrribute):
    return getattr(obj,atrribute)
