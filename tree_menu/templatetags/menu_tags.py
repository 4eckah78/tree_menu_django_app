
from django import template
from django.urls import resolve
from django.utils.safestring import mark_safe

from tree_menu.models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    items = menu.items.filter(parent=None)

    def is_active(item):
        url = item.get_url()
        if url and resolve(current_path).url_name == resolve(url).url_name:
            return True
        return any(is_active(child) for child in item.children.all())

    def render_items(items, depth=0):
        html = '<ul>'
        for item in items:
            active = is_active(item)
            css = 'active' if active else ''
            html += f'<li class="{css}"><a href="{item.get_url()}">{item.title}</a>'
            children = item.children.all()
            if active or depth==0:
                html += render_items(children, depth+1)
            html += '</li>'
        html += '</ul>'
        return html

    return mark_safe(render_items(items))
