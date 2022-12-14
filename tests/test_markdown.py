from invisibleroads_macros_web.markdown import (
    get_html_from_markdown)


def test_get_html_from_markdown():
    html = get_html_from_markdown('x')
    assert not html.startswith('<p>') and not html.endswith('</p>')
    html = get_html_from_markdown('x\n\nx')
    assert html.startswith('<p>') and html.endswith('</p>')
    html = get_html_from_markdown('x\n\n<button></button>\n\nx')
    assert '<p><button></button></p>' not in html
    html = get_html_from_markdown('x\n\n<button></button>\n\n<a></a>.')
    assert '<p><a></a>.</p>' in html
