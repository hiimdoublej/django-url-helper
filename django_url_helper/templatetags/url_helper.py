# -*- coding: utf-8 -*-
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from django import template
from .. import utils

register = template.Library()


@register.simple_tag
def add_param(url, key, value):
    return utils.add_param(url, key, value)


@register.simple_tag
def toggle_param(url, key, value):
    return utils.toggle_param(url, key, value)


@register.simple_tag
def reset_param(url, key, value):
    return utils.reset_param(url, key, value)


@register.simple_tag
def remove_param(url, key, value):
    return utils.remove_param(url, key, value)


@register.simple_tag
def purge_param(url, key):
    return utils.purge_param(url, key)
