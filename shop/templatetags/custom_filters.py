from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.filter
def get_attr(obj, atrribute):
    return getattr(obj,atrribute)

@register.filter
def get_attr_or_render(model, attribute):
    if  attribute[-5:] == ".html":
        return render_to_string(attribute, {"model":model}) # Where attribute is template name
    else:
        return getattr(model,attribute) # Where attribute is model field name
