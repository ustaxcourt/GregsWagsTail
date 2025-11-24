from django import template
from home.models import FooterText

register = template.Library()


@register.simple_tag
def get_footer_text():
    return FooterText.objects.first()
