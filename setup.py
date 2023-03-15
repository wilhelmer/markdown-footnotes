from setuptools import setup

setup(
    name='markdown-footnotes',
    version='0.1.1',
    description= 'The official Python-Markdown "footnotes" extension, with additional options.',
    long_description='',
    url='https://github.com/wilhelmer/markdown-footnotes.git',
    author='Lars Wilhelmer',
    author_email='lars@wilhelmer.de',
    license='MIT',
    packages=['footnotes2'],
    keywords="markdown footnotes",
    install_requires=['Markdown>=3.0.1']
)
