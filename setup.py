from os.path import abspath, dirname, join
from setuptools import find_packages, setup


ENTRY_POINTS = '''
'''
FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, _)).read().strip() for _ in [
    'README.md', 'CHANGES.md'])


setup(
    name='invisibleroads-macros-web',
    version='0.2.2',
    description='Shortcut functions for web operations',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
    author='Roy Hyunjin Han',
    author_email='rhh@crosscompute.com',
    url=(
        'https://github.com/invisibleroads/'
        'invisibleroads-macros-web'),
    keywords='invisibleroads',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['invisibleroads-macros-process'],
    extras_require={
        'jinja': ['jinja2'],
        'markdown': ['markdown'],
        'starlette': ['starlette'],
        'test': ['pytest', 'pytest-cov'],
    },
    entry_points=ENTRY_POINTS)
