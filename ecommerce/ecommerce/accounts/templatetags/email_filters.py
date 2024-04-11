from django import template

register = template.Library()


@register.filter(name='username')
def get_email_username(value):
    return value.split('@')[0]
