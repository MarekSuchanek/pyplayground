from setuptools import setup, find_packages

setup(
    name='pyplayground',
    version='0.0',
    keywords='testing nothing',
    description='Just for testing Python and some tools',
    long_description='',
    author='Marek Suchánek',
    author_email='suchama4@fit.cvut.cz',
    license='MIT',
    url='https://github.com/MarekSuchanek/pyplayground',
    packages=find_packages(),
    install_requires=[
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest-pep8',
        'pytest-cov',
        'pytest'
    ],
)
