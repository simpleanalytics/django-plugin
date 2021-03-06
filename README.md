<a href="https://simpleanalytics.com/?ref=github.com/simpleanalytics/django-plugin">
  <img src="https://assets.simpleanalytics.com/images/logos/logo-github-readme.png" alt="Simple Analytics logo" align="right" height="62" />
</a>

# Django Plugin

Want privacy friendly analytics for Django? You're at the right place.

> You need an account [on Simple Analytics](https://simpleanalytics.com) to see your stats collected by this plugin.

## Installing it

Install the plugin:

`pip install simpleanalytics`

## Using it

Add the package to the `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
   ...,
   simpleanalytics,
]
```

Next use the `templatetag` in your template:

```
<!DOCTYPE html>
{% load static simpleanalytics_tags %}
<html>
	<head>
		<meta charset="utf-8">
		<title>{% block page_title %}{{ site.name }}{% endblock %}</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    ...
    {% simpleanalytics_sync %}
    ...
    </head>
    <body>
      {% simpleanalytics_noscript_block %}
    </body>
</html>
```

This will translate to roughly this:
```
<!DOCTYPE html>

<html>
	<head>
		<meta charset="utf-8">
		<title>brwnppr.com</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    ...
    <script type="text/javascript" src="https://cdn.simpleanalytics.io/hello.js"></script>
    ...
    </head>
    <body>
      <noscript><img src="https://api.simpleanalytics.io/hello.gif" alt="hello"></noscript>
    </body>
</html>
```

## More

This app has four templatetags:

- simpleanalytics_sync
- simpleanalytics_async
- simpleanalytics_noscript_block
- simpleanalytics_noscript_img

`simpleanalytics_sync` converts to a plain `<script>` tag without the `async`
keyword.

`simpleanalytics_async` converts to a plain `<script>` tag with the `async`
keyword.

`simpleanalytics_noscript_block` converts to an `<noscript>` block which
includes an `img` element which is used to load the image. Use this when you
don't have and don't need a `<noscript>` block on your page at all.

`simpleanalytics_noscript_img` converts to an `<img>` tag which src points to
the hello.img. Use this when you're using a `<noscript>` block and you want to
add privacy friendly stats to your page.

## Compatibility

Tested on Django 2.2, but we think this should run on any recent Django 
deployment. Please raise an issue when it doesn't.


