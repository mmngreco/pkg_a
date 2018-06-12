from setuptools import setup

setup(
        name='pkg_a',
        install_requires=[],
        packages=['pkg_a'],
        extras_require={'np': ['numpy'], 'pd': ['pandas']},
        )

