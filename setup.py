from setuptools import setup, find_packages

setup(
    name='Takeshi castle',
    author='Adrian Bayona',
    description='CLI videogame in python',
    author_email='ronaldo13_96@outlook.com',
    version='1.0',
    packages= (find_packages()),
    install_requires = [
        'click==8.1.3',
        'click-help-colors==0.9.1',
        'colorama==0.4.5',
        'commonmark==0.9.1',
        'docutils==0.19',
        'halo==0.0.31',
        'log-symbols==0.0.14',
        'Pygments==2.13.0',
        'rich==12.5.1',
        'six==1.16.0',
        'spinners==0.0.24',
        'termcolor==2.0.1',
        'wincertstore==0.2',
    ],
    entry_points={
    'console_scripts': ['castle= CastleGame.Castle:main'],
    },
)