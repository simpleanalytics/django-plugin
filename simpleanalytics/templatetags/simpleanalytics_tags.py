"""

(c) 2019 by simpleanalytics.io. All rights reserved

This program is distributed in the hope that it will be useful, but is provided AS IS with ABSOLUTELY NO WARRANTY;
The entire risk as to the quality and performance of the program is with you. Should the program prove defective,
you assume the cost of all necessary servicing, repair or correction. In no event will any of the developers, or
any other party, be liable to anyone for damages arising out of the use or inability to use the program.
You may copy and distribute copies of the Program, provided that you keep intact all the notices that refer to the
absence of any warranty.

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
