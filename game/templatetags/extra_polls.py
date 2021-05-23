from django import template
from django.utils.safestring import mark_safe
import json
register = template.Library()

# @register.filter(name = 'rounder')
# def rounder(value, arg):
#     """Removes all values of arg from the given string"""
#     return round(float(value),int(arg))

_js_escapes = {
    ord('\\'): '\\u005C',
    ord('\''): '\\u0027',
    ord('"'): '\\u0022',
    ord('>'): '\\u003E',
    ord('<'): '\\u003C',
    ord('&'): '\\u0026',
    ord('='): '\\u003D',
    ord('-'): '\\u002D',
    ord(';'): '\\u003B',
    ord('`'): '\\u0060',
    ord('\u2028'): '\\u2028',
    ord('\u2029'): '\\u2029'
}

# Escape every ASCII character with a value less than 32.
_js_escapes.update((ord('%c' % z), '\\u%04X' % z) for z in range(32))

@register.filter(name = 'convertJSON')
def convertJSON(value):
    return mark_safe(str(json.dumps(value)).translate(_js_escapes))

@register.filter(name = 'booleanConvert')
def booleanConvert(value):
    return str(value).lower()

@register.filter(name = 'replace_split')
def replace_split(value, pon):
    value = value.replace('POSITION1', pon.split(',')[0])
    value = value.replace('POSITION2', pon.split(',')[1])
    return value
