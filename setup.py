import setuptools

setuptools.setup(
    name="telelib",
    description="A Telegram Wrapper Written in ?",
    author="Mohammad Mahdi Afshar",
    author_email="me@mamad.dev",
    version=open("VERSION").read().strip(),
    license="The Unlicensed",
    packages=setuptools.find_packages(),
    dependencies=[
        "thread_py",
        "xhttp",
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
