from setuptools import setup, find_packages

setup(
    name='paper-fetcher',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line application to fetch academic papers from various sources.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'paper-fetcher=cli:main',
        ],
    },
)