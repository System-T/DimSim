from setuptools import setup

setup(name='dimsim',
	version='1.0',
	description='Python implementation of the Chinese soundex project DimSim',
	author='IBM SystemT, IBM CODAIT',
	author_email='qian.kun@ibm.com, karthik.muthuraman@ibm.com, ihjhuo@ibm.com, frreiss@us.ibm.com',
	 url='https://github.com/System-T/DimSim',
	packages=['dimsim', 'dimsim.core', 'dimsim.utils', 'dimsim.data'],
	package_data={'':['dimsim/data/pinyin_to_simplified.pickle','dimsim/data/pinyin_to_traditional.pickle']},
	include_package_data=True,
	classifiers=["License :: OSI Approved :: Apache 2.0 License"],
	install_requires=[
        'pypinyin',
        ],
	test_suite='nose.collector',
    tests_require=['nose']
)
