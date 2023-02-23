"""Setup module for pydracor

See: https://github.com/dracor-org/pydracor
"""
from setuptools import setup

# Get the long description from the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydracor',
    packages=['pydracor'],
    version='1.0.0',
    license='mit',
    description='Python package which provides access to the DraCor API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eduard Grigoriev, Henny Sluyter-Gäthje',
    author_email='sluytergaeth@uni-potsdam.de, happypuffin7@gmail.com',
    url='https://github.com/dracor-org/pydracor',
    keywords=['drama corpus', 'drama', 'corpus', 'pydracor', 'dracor', 'api', 'wrapper'],
    install_requires=[
        'requests>=2.28.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
