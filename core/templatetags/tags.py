import urllib

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, request, page=1):
    """
    Used in pagination, not for single used
    """
    query = request.dict()
    query['page'] = page
    return urllib.parse.urlencode(query)


@register.inclusion_tag('inclusions/pagination.html', takes_context=True)
def pagination(context):
    """
    Vorks with generic views which have object_list in their context
    as that models QuerySet
    USE: {% pagination %}
    """
    return {
        'paginate_by': context['object_list'],
        'request': context['request'].GET
    }
