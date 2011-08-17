from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if '/' == pattern:
        if '/'  == request.path:
            return 'class="on"'
    elif re.match(pattern, request.path):
        return 'class="on"'
    return ''
