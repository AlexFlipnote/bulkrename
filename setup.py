import re

from setuptools import setup


version = ''
with open('bulkrename/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


if not version:
    raise RuntimeError('version is not set')


setup(
    name='bulkrename',
    author='AlexFlipnote',
    url='https://github.com/AlexFlipnote/bulkrename',
    version=version,
    packages=['bulkrename'],
    license='GNU v3',
    description='Rename multiple files in a folder to random characters',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bulkrename=bulkrename.bulkrename:main',
            'bulkrn=bulkrename.bulkrename:main'
        ]
    }
)
