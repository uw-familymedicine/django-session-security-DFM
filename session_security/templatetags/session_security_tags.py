from django import template
from django.conf import settings
from django.urls import reverse, resolve, Resolver404
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


@register.filter
def redirect_to_logout(request):
    current_url = resolve(request.path_info).url_name
    if current_url == 'aa_forms_edit':
        redirect = False
        return redirect
    else:
        redirect = getattr(settings, 'SESSION_SECURITY_REDIRECT_TO_LOGOUT', False)
        return redirect