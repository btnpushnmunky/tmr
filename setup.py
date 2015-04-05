from setuptools import setup, find_packages

setup(
    name='tmr',
    version='0.5.0',
    description='Command line application for keeping track of time.',
    author='Dan Ross',
    author_email='dan@rosspixelworks.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['Click', 'Peewee'],
    entry_points={
        'console_scripts': [
            'tmr-init=tmr.main:init',
            'tmr-start=tmr.main:start'
        ],
    },
    )
