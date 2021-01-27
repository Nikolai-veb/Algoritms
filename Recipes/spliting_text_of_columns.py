s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
>>> print(textwrap.fill(s, 70))
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes, you're under.

>>> print(textwrap.fill(s, 40, initial_indent=' '))
 Look into my eyes, look into my
eyes, the eyes, the eyes, the eyes, not
around the eyes, don't look around the
eyes, look into my eyes, you're under.
>>> print(textwrap.fill(s, 40, subsequent_indent=' '))
Look into my eyes, look into my eyes,
 the eyes, the eyes, the eyes, not
 around the eyes, don't look around
 the eyes, look into my eyes, you're
 under.
 
К вопросу о размере терминала: вы можете получить его, используя os.get_terminal_size(). Например:
>>> import os
>>> os.get_terminal_size().columns
80
