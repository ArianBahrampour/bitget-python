from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = 'This is a lightweight library that works as a connector to Bitget pulic API'
LONG_DESCRIPTION = 'SDK for bitget exchange supporting rest and websocket API.'

setup(
    name="bitget-connector",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Arian Bahrampour",
    author_email="dev.arianbahrampour1380@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'bitget', 'sdk', 'api', 'wrapper'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
