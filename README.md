# simpleanalytics for Django
Want privacy friendly analytics for Django? You're at the right place.

# Installing it
Install the plugin:

`pip install django-simpleanalytics`

# Using it
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
{% load staticfiles simpleanalytics_tags %}
<html>
	<head>
		<meta charset="utf-8">
		<title>{% block page_title %}{{ site.name }}{% endblock %}</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    ...
    {% simple_analytics_sync %}
    ...
    </head>
    <body>
      {% simple_analytics_noscript_block %}
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

# More

This app has four templatetags:

- simple_analytics_sync
- simple_analytics_async
- simple_analytics_noscript_block
- simple_analytics_noscript_img 

`simple_analytics_sync` converts to a plain `<script>` tag without the `async`
keyword. 

`simple_analytics_async` converts to a plain `<script>` tag with the `async`
keyword. 

`simple_analytics_noscript_block` converts to an `<noscript>` block which 
includes an `img` element which is used to load the image. Use this when you 
don't have and don't need a `<noscript>` block on your page at all. 

`simple_analytics_noscript_img` converts to an `<img>` tag which src points to
the hello.img. Use this when you're using a `<noscript>` block and you want to
add privacy friendly stats to your page.

# Compatibility

Tested on Django 2.2.


