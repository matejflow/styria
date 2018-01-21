from django import template

register = template.Library()


@register.inclusion_tag('inclusions/top_movies.html', takes_context=True)
def widget_top_movies(context):
    """
    Shows top movies as a sidebar widget

    USE: {% widget_top_movies %}
    """
    return {
        'top_movies': context['top_movies'],
    }
