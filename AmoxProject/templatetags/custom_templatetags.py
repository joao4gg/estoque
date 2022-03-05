from django import template
register = template.Library()


@register.filter
def bool_value(value):
    if value in (1, True, 'True'):
        return 'Sim'
    else:
        return 'Não'


@register.filter
def null_value(value):
    if value is None or value == 'None':
        return ''
    else:
        return value