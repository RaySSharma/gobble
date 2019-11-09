from setuptools import setup

VERSION = '0.1.0'

setup(
    name='gobbler',
    version=VERSION,
    py_modules=['gobble'],
    url='https://github.com/rayssharma/gobble',
    download_url='https://github.com/rayssharma/gobble/tarball/{}'.format(VERSION),
    license='MIT',
    author='Ray Sharma',
    author_email='ramon.sharma1@gmail.com',
    description='Turkey-themed image catalog to boost the holiday mood.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['pillow==5.2.0'],
    entry_points={
        'console_scripts': ['gobble=gobble:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)