from setuptools import setup, find_packages

setup(
    name="contactWho",
    version='0.1',
    description='Contact Book',
    author='78RainDrops',
    author_email='smileyrence3@gmail.com',
    packages=find_packages(),
    entry_points = {
        'console_scripts' : [
            'contactWho=contact_who.contact:main'
        ],
    },
    install_requires=[
        'requests',
    ],
)