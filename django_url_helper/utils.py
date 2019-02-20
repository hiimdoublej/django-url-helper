# -*- coding: utf-8 -*-
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit


def add_param(url, key, value):
    o, q = parse_url(url)
    current_values = q.get(key)
    if current_values:
        q[key].append(value)
    else:
        q[key] = value
    return reconstruct_url(o, q)


def toggle_param(url, key, value):
    o, q = parse_url(url)
    current_values = q.get(key)
    if current_values:
        if value in current_values:
            return remove_param(url, key, value)
    return add_param(url, key, value)


def reset_param(url, key, value):
    o, q = parse_url(url)
    q[key] = value
    return reconstruct_url(o, q)


def remove_param(url, key, value):
    o, q = parse_url(url)
    current_values = q.get(key)
    if not current_values:
        return reconstruct_url(o, q)
    if value in current_values:
        q[key].remove(value)
    return reconstruct_url(o, q)


def purge_param(url, key):
    o, q = parse_url(url)
    if key in q.keys():
        del q[key]
    return reconstruct_url(o, q)


def parse_url(url):
    o = urlsplit(url)
    q = parse_qs(o.query)
    return o, q


def reconstruct_url(o, q):
    new_query = urlencode(q, doseq=True)
    return urlunsplit((o.scheme, o.netloc, o.path, new_query, o.fragment))


def is_int(target):
    try:
        int(target)
        return True
    except ValueError:
        return False
