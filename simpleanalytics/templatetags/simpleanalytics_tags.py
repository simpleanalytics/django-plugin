"""

MIT License

Copyright (c) 2019 by Simple Analytics. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


_script_element = 'https://cdn.simpleanalytics.io/hello.js'
_img_element = 'https://api.simpleanalytics.io/hello.gif'


register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        '<script type="text/javascript" src="{script}"></script>'.format(
            script=_script_element,
        )
    ),
    name='simpleanalytics_sync',
)


register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        '<script async type="text/javascript" src="{script}"></script>'.format(
            script=_script_element,
        )
    ),
    name='simpleanalytics_async',
)


# Installs the simpleanalytics noscript pixel wrapped in an noscript block
register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        '<noscript><img src="{img}" alt=""></noscript>'.format(
            img=_img_element,
        ),
    ),
    name='simpleanalytics_noscript_block',
)

# Installs the simpleanalytics noscript pixel in an image element
register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        '<img src="{img}" alt="">'.format(
            img=_img_element,
        ),
    ),
    name='simpleanalytics_noscript_img',
)
