from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def into_admin(obj):
    if not hasattr(obj, '_meta'):
        return reverse('main')
    return reverse('admin:%s_change' % (obj._meta.db_table), args=(obj.id,))
