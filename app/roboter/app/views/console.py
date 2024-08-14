import os
import string
import termcolor

def get_template_dir_path():
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass
    
    if not template_dir_path:
        # このファイルの2つ上のディレクトリ
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path

class NoTemplateError(Exception):
    pass

def find_template(template_file):
    template_dir_path = get_template_dir_path()
    template_file_path = os.path.join(template_dir_path, template_file)
    if not os.path.exists(template_file_path):
        raise NoTemplateError('Could not find {}'.format(template_file))
    return template_file_path

def get_template(template_file_path, color=None):

    template = find_template(template_file_path)

    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep) # osの改行コードを取り除く
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(contents=contents, splitter="=" * 60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)