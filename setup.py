from setuptools import setup

setup(
    name='internal-utils',
    version='0.0.5',
    description='internal utility methods',
    packages=[
        'internal',
        'internal.test',
        'internal.test.factories'
    ],
    install_requires=[
        'flask',
        'faker'
    ]
)
