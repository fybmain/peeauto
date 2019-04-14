from setuptools import setup, find_packages
import pypandoc

setup(
    name='peeauto',
    version=0.1,
    description=(
        'Automatic CRUD model framework'
    ),
    long_description=pypandoc.convert_file('README.md', 'rst'),
    author='fyb',
    author_email='fybmain@gmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/fybmain/peeauto',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'peewee>=3.9.3',
    ],
)
