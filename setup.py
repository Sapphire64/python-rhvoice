from distutils.core import setup

setup(
    name='python-rhvoice',
    version='1.0.0',
    author='Anton Vlasenko',
    author_email='antares.spica@gmail.com',
    packages=['rhvoice'],
    scripts=[],
    #url='http://pypi.python.org/pypi//',
    license='LICENSE.txt',
    description='Python bindings for RHVoice library.',
    long_description=open('README.rst').read(),
    install_requires=[],
)