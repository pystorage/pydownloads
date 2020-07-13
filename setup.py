from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydownloads',
    version='0.1.0',
    author='PyMaster',
    author_email='',
    description='Statistics download python packages PiPy.',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='statistics download python PiPy',
    url='https://github.com/pystorage/pydownloads',
    packages=['pydownloads'],
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
