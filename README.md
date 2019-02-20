Django Url Helper
===
Helper function and template tags for dealing with numeric url query strings in Django.

Install
---
1. `pip install django_url_helper`
2. Add `django_url_helper` to your `INSTALLED_APPS`
3. You're all set!

Basic Usage
---

In templates:
put `{% load url_helper %}` on top of your template.
given a variable in template `url` which resolves into `https://some.django.site/somepath/?k=1`
The following steps are applied and demostrated in order.
1. Applying `{% add_param url 'page' '1' %}` would resolve into  `https://some.django.site/somepath/?k=1&page=1`
2. Then, `{% toggle_param url 'page' '1' %}` would toggle off the `page=1`, resolving into `https://some.django.site/somepath/?k=1`
3. Then, `{% toggle_param url 'page' '1' %}` would toggle on the `page=1` , which would resolve into `https://some.django.site/somepath/?k=1&page=1`
4. Then, `{% reset_param url 'k' '2' %}` would reset `k` to value `2`, resolves to `https://some.django.site/somepath/?k=2&page=1`
5. Then, `{% remove_param url 'k' '2' %}` would remove any `k=2` query string in target url. In our case this would resolve into `https://some.django.site/somepath/?page=1`
6. Finally, `{% purge_param url 'page' %}` would remove any query string with key `page`, this will give us `https://some.django.site/somepath/`

Contibuting
---
Tests are ran using `pytest`, any contibutions are welcomed.
