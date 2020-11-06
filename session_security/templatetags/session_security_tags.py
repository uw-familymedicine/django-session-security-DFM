from django import template

from session_security.settings import YAR_WARN_AFTER, WARN_AFTER, YAR_EXPIRE_AFTER, EXPIRE_AFTER

register = template.Library()


@register.filter
def expire_after(request):
    current_url = resolve(request.path_info).url_name
    if current_url == 'aa_forms_edit':
        return YAR_EXPIRE_AFTER
    else:
        return EXPIRE_AFTER


@register.filter
def warn_after(request):
    current_url = resolve(request.path_info).url_name
    if current_url == 'aa_forms_edit':
        return YAR_WARN_AFTER
    else:
        return WARN_AFTER