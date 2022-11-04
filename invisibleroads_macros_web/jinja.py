from os.path import dirname, getmtime, join, normpath, realpath

from jinja2 import BaseLoader, Environment, TemplateNotFound, pass_context


class DictionaryTemplateLoader(BaseLoader):

    def __init__(self, template_path_by_id, encoding='utf-8'):
        self.template_path_by_id = template_path_by_id
        self.encoding = encoding

    def get_source(self, environment, template):
        path = str(self.template_path_by_id[template])
        try:
            modification_time = getmtime(path)
        except OSError:
            raise TemplateNotFound(path)

        def is_latest():
            try:
                return modification_time == getmtime(path)
            except OSError:
                return False

        with open(path, mode='rt', encoding=self.encoding) as f:
            text = f.read()
        return text, realpath(path), is_latest


class RelativeTemplateEnvironment(Environment):

    def join_path(self, template, parent):
        'Support relative template paths via extends, import, include'
        return normpath(join(dirname(parent), template))


@pass_context
def url_for(context, name, **d):
    return context['request'].url_for(name, **d)
