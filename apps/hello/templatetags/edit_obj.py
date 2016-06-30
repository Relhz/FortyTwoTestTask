from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(obj):
    if not hasattr(obj, '_meta'):
        url = reverse('main')
        return '<a href="{0}">'.format(url) + \
            str(obj) + '</a>'
    url = reverse('admin:%s_change' % (obj._meta.db_table), args=(obj.id,))
    return '<a href="{0}">'.format(url) + str(obj) + '</a>'
