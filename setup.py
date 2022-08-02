import setuptools

import telelib

setuptools.setup(
    name="telelib",
    description="A Telegram Wrapper Written in ?",
    author="Mohammad Mahdi Afshar",
    author_email="me@mamad.dev",
    version=telelib.__VERSION__,
    license="The Unlicensed",
    packages=setuptools.find_packages(),
    requires=[
        "thread_py",
        "httpx",
        "requests",
        "coloredlogs"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
