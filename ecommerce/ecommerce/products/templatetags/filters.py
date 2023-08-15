from django import template

register = template.Library()


@register.filter
def generate_range(value):
    return range(1, value + 1)


@register.filter
def get_lesser(value, arg):
    return min(value, arg)
