import pathlib

import setuptools


setuptools.setup(
    name='lektor-summernote',

    use_scm_version=True,

    author='Monette Gordon, Miguel Jacq',
    author_email='monette@mydex.org',
    maintainer='Monette Gordon',
    maintainer_email='monette@mydex.org',

    description='Plugin integrating Summernote into Lektor admin editor',
    keywords='Lektor admin plugin Summernote wysiwyg editor',
    license='MIT',
    long_description_content_type='text/html',

    packages=setuptools.find_packages(),
    py_modules=['lektor_summernote'],

    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],

    entry_points={
        'lektor.plugins': [
            'summernote = lektor_summernote:SummernotePlugin',
        ],
    },
)