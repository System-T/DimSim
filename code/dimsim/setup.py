from setuptools import setup

setup(name="dimsim",
	version="0.1",
	description="Python implementation of Chinese soundex",
	author="Kun Qian",
	author_email="qian.kun@ibm.com",
	packages=['dimsim'],
	package_data={"":['pinyin_to_simplified.pickle','pinyin_to_traditional.pickle']},
	include_package_data=True,
	classifiers=["License :: OSI Approved :: Apache 2.0 License"]
)

