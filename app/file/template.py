import string

s = """\

Hi $name.

$contents

Have a good day
"""
with open('./file/email_template.txt') as f:
  t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)