from optparse import OptionParser
from optparse import OptionGroup


def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    # parser.add_option('-f', '--file', action='store', type='string',
    #                   dest='filename', help='File name')

    # python basic/parser.py -f test.txt a b
    # 実行結果
    # {'filename': 'test.txt'}
    # ['a', 'b']

    # parser.add_option('-n', '--num', action='store', type='int', dest='num')

    # python basic/parser.py -f test.txt a b
    # 実行結果
    # {'num': 10}
    # ['a', 'b']

    # parser.add_option('-v', action='store_true', dest='verbose')
    # python basic/parser.py -v
    # {'verbose': True}
    # []
    # store_falseならFalse

    # parser.add_option('-v', action='store_true', dest='verbose')
    # parser.add_option('-q', action='store_true', dest='verbose')
    # parser.set_defaults(verbose=True)
    # python basic/parser.py
    # {'verbose': True}
    # []

    # parser.add_option('-r', action='store_const', const='root',
    #                   dest='user_name')
    # {'user_name': 'root'} constの値が入る
    # []

    # parser.add_option('-e', dest='env')

    # def is_release(option, opt_str, value, parser):
    #     if parser.values.env == 'prd':
    #         raise parser.error("Can't release")
    #     setattr(parser.values, option.dest, True)
    # parser.add_option('--release', action='callback', callback=is_release,
    #                   dest='release')

    # python basic/parser.py -e prd --release
    # Usage: parser.py [options] arg1 arg2
    # parser.py: error: Can't release

    # python basic/parser.py -e test --release
    # {'env': 'test', 'release': None}
    # []

    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    # python basic/parser.py -g
    # {'g': True}
    # []

    options, args = parser.parse_args()
    print(options)
    print(args)


if __name__ == '__main__':
    main()
