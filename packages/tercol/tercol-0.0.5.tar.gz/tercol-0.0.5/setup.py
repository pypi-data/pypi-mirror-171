from ast import keyword
from setuptools import setup, find_packages
classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='tercol',
    version='0.0.5',
    description='TerCol is a useless library that colors your text.',
    url='https://github.com/Butterroach/tercol/',
    author='Sultan Marzouq',
    author_email='epicnoobcontactemail@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='terminal styling, colors, style',
    packages=find_packages(),
    install_requires=[''],
    download_url = 'https://github.com/Butterroach/tercol/archive/refs/tags/v_005.tar.gz'
)