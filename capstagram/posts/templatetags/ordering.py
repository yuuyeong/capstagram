from django import template
from posts.utils import post_order_by


register = template.Library()


@register.filter
def ordering(value):
    return post_order_by(value)
