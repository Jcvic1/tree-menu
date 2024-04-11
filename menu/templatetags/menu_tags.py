from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from menu.models import Menu


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_path = context['request'].path
    menu_items = Menu.objects.filter(parent__isnull=True, title=menu_name)
    return render_menu(menu_items, current_path)


def render_menu(menu_items, current_path, parent_expanded=False):
    if menu_items:
        result = '<ul class="menu">'
        for item in menu_items:
            children = Menu.objects.filter(parent=item)
            url = reverse('menu', args=[item.title])
            is_expanded = parent_expanded or current_path.startswith(url)
            result += f'<li class="menu-item" data-url="{url}">'
            if children:
                result += f'<i class="toggle-btn me-1 bi bi-plus-circle text-light"></i>'
            else:
                result += f'<i class="me-1 bi bi-circle text-light"></i>'
            result += f'<button class="text-btn">{item.title}</button>'
            if children:
                result += render_submenu(children, current_path, is_expanded)
            result += '</li>'
        result += '</ul>'
        return mark_safe(result)
    return ''

def render_submenu(menu_items, current_path, parent_expanded=False):
    result = '<ul class="submenu">'
    for item in menu_items:
        children = Menu.objects.filter(parent=item)
        url = reverse('menu', args=[item.title])
        is_expanded = parent_expanded or current_path.startswith(url)
        result += f'<li class="menu-item" data-url="{url}">'
        if children:
            result += f'<i class="toggle-btn me-1 bi bi-plus-circle text-light"></i>'
        else:
            result += f'<i class="me-1 bi bi-circle text-light"></i>'
        result += f'<button class="text-btn">{item.title}</button>'
        if children:
            result += render_submenu(children, current_path, is_expanded)
        result += '</li>'
    result += '</ul>'
    return result
        

