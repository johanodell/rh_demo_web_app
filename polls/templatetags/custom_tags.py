from django import template
register = template.Library()

import socket

@register.simple_tag
def get_hostname():
    return socket.gethostname()
