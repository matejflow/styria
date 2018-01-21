from django import template

register = template.Library()


@register.filter(is_safe=True)
def tooltip(tooltip_text):
    tooltip = '''<div class="info-help">
        <i class="material-icon help"></i>
        <p class="content">{}</p>
    </div>'''.format(tooltip_text)
    return tooltip
    # use it like this: {{"Put text here"|tooltip}}
