from setuptools import setup

setup(
    name='pyglotz',
    version='0.1.0',
    description='Python interface to the Glotz API (www.glotz.info)',
    url='https://github.com/3OW/pyglotz',
    author='3OW',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
    ],

    keywords='glotz',
    packages=['pyglotz'],
    install_requires=['requests']
)
