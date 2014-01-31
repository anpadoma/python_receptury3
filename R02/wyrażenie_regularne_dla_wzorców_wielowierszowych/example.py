# example.py
#
# Wyrażenie regularne dla wzorców wielowierszowych

import re

text = '''/* To jest
              komentarz wielowierszowy */
'''

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text))
