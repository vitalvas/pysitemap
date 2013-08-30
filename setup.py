from setuptools import setup

setup(
	name='pysitemap',
	version=0.5,
	description='A Python library for generating sitemap',
	long_description=open('README.rst').read(),
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python',
		'Topic :: Software Development',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7'
	],
	platforms='any',
	keywords='sitemap xml',
	author='VitalVas',
	url='https://github.com/vitalvas/pysitemap',
	license='BSD',
	py_modules=['pysitemap']
)
