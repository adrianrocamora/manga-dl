from __future__ import print_function

from setuptools import setup
from glob import glob
from MangaDL.meta import __version__, __downloader_uri__


REQUIREMENTS = [
    'setuptools',
    'lxml>=3.7.2',
    'cssselect>=1.0.0',
    'Pillow>=4.3',
    'requests>=2.14',
    'pycrypto>=2.5',
    'cfscrape>=1.9.1',
    'progressbar2>3.34',
    'html-purifier>=0.1.9',
    'urllib3',
    'packaging',
]

setup(
    name='MangaDL',
    packages=[
        'MangaDL',
        'MangaDL.base_classes',
        'MangaDL.crypt',
        'MangaDL.gui',
        'MangaDL.http',
        'MangaDL.providers',
        'MangaDL.providers.helpers',
        'MangaDL.server',
    ],
    include_package_data=True,
    version=__version__,
    description='Universal assistant download manga.',
    author='Zharkov Sergey',
    author_email='sttv-pc@mail.ru',
    url=__downloader_uri__,
    zip_safe=False,
    data_files=[
        ('MangaDL/gui/langs', glob('MangaDL/gui/langs/*.json'))
    ],
    download_url='{}/archive/{}.tar.gz'.format(__downloader_uri__, __version__),
    keywords=['manga-downloader', 'manga'],
    license='MIT',
    classifiers=[  # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.5',
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'manga-dl = MangaDL:main',
        ]
    }
)