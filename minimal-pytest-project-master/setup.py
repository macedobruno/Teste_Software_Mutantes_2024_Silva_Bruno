from setuptools import setup, find_packages

import mymath

setup(
    name=mymath.__name__,
    version=mymath.__version__,
    author='Bruno Macedo',
    author_email='brunoms@dcomp.ufs.br',
    description='Example for a minimal Python project with pytest support',
    packages=find_packages(),
    install_requires=[],  # e.g. ['numpy >= 1.11.1', 'matplotlib >= 1.5.1']
)

