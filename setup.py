from setuptools import setup

setup(
    name='boot',
    version='1.0.0',
    py_modules=['app'],
    install_requires=['Click'],
    entry_points='''
    [console_scripts]
    boot=boot:app
    ''',
)

