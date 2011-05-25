from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        print pattern
        print request.path
        return 'class="on"'
    return ''
