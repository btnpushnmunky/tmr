from setuptools import setup

setup(
    name='tmr',
    version='0.5.0',
    description='Command line application for keeping track of time.'
    author='Dan Ross',
    author_email='dan@rosspixelworks.com',
    license='MIT',
    py_modules='tmr',
    install_requires=['Click', 'pewee']
    entry_points={
        'console_scripts': [
            'tmr-init=tmr:init',
        ],
    },
    )
