import re

# RE_STACK_ID = re.compile(
#         (r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
#          r':stack/(?P<stack_name>[\w-]+)/[\w-]+'))


# 正規表現を自由に定義できる
RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):      # region
    (?P<account_id>[\d]+):    # account_id
    stack/
    (?P<stack_name>[\w-]+)/  # stack_name
    [\w-]+""", re.VERBOSE)

s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
      'mystack-mynestedstack-sggfrhxhm7w/f449b250-b969-lle0-a185-5081d016786')

s2 = ('arn:aws:cloudformation:us-east-1:888856789012:stack/'
      'mystack-mynestedstack-sggfrhxabcs7w/f449b250-b969-lle0-a185-5081d01786')

for s in [s1, s2]:

    # m = re.match(
    #     (r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
    #      r':stack/(?P<stack_name>[\w-]+)/[\w-]+'), s)
    m = RE_STACK_ID.match(s)

    if m:
        print('go next')
        print(m)
        print(m.group())
        print(m.group('region'))
        print(m.group('account_id'))
        print(m.group('stack_name'))
