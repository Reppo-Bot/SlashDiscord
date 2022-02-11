from setuptools import find_packages, setup
setup(
    name='slashReppo',
    packages=find_packages(include=['slashReppo']),
    version='0.0.1',
    description='Discord slash command wrapper',
    author='Josh Brown, Matt Dray',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
