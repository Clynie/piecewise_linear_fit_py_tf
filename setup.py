from setuptools import setup

setup(
    name='pwlftf',
    version='1.0.0',
    author='Charles Jekel',
    author_email='cjekel@gmail.com',
    packages=['pwlftf'],
    url='https://github.com/cjekel/piecewise_linear_fit_py_tf',
    license='MIT License',
    description='fit piecewise linear functions to data',
    long_description=open('README.rst').read(),
    platforms=['any'],
    install_requires=[
        "numpy >= 1.14.0",
        "scipy >= 1.2.0",
        "pyDOE >= 0.3.8",
        "setuptools >= 38.6.0",
        "tensorflow < 2.0.0"
    ]
)
