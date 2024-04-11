from django import template

WIDGET_TYPES = (
    'text',
    'number',
    'email',
    'url',
    'password',
    'textarea',
)

register = template.Library()


@register.simple_tag
def get_field_classes(field):
    if field.widget_type not in WIDGET_TYPES:
        return ''

    field_classes = ['default']

    if field.form.is_bound:
        if field.errors:
            field_classes.append('invalid')
        else:
            field_classes.append('valid')

    return ' '.join(field_classes)
