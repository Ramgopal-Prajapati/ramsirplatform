from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary by key - used in templates as dict|get_item:key"""
    if isinstance(dictionary, dict):
        return dictionary.get(key, False)
    return False

@register.filter
def subtract(value, arg):
    return int(value) - int(arg)
