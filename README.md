<a href="https://www.simpleanalytics.com/?ref=github.com/simpleanalytics/django-plugin">
  <img src="https://assets.simpleanalytics.com/images/logos/logo-github-readme.png" alt="Simple Analytics logo" align="right" height="62" />
</a>

# Django Plugin

Want privacy friendly analytics for Django? You're at the right place.

> You need an account [on Simple Analytics](https://www.simpleanalytics.com) to see your stats collected by this plugin.

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
    <script type="text/javascript" src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
    ...
    </head>
</html>
```

## More

This app has four templatetags:

- simpleanalytics_sync
- simpleanalytics_async

`simpleanalytics_sync` converts to a plain `<script>` tag without the `async`
keyword.

`simpleanalytics_async` converts to a plain `<script>` tag with the `async`
keyword.

## Compatibility

Tested on Django 2.2, but we think this should run on any recent Django 
deployment. Please raise an issue when it doesn't.


