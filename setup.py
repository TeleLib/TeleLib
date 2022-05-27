from setuptools import setup


setup(
	name='telelib',
	version='6.0.0',
	description='A Telegram Wrapper',
	author='Mohammad Mahdi Afshar',
	author_email="me@mamad.dev",
	url='https://github.com/reloadlife/telelib',
	packages=[
		'telelib'
	],
	install_requires=[
		'requests',
	],
)