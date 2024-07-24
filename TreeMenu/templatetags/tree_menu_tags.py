from TreeMenu.models import TreeMenu
from django import template

register = template.Library()


@register.inclusion_tag('TreeMenu/draw_menu.html')
def draw_menu(slug=None):
    if slug:
        items = TreeMenu.objects.filter(slug=slug).select_related('parent')
    else:
        items = TreeMenu.objects.filter(parent__isnull=True).select_related('parent')

    return {
        'menu_items': items,
    }
