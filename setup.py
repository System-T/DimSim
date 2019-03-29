from setuptools import setup

setup(name='max-chinese-soundex',
	version='0.1',
	description='Python implementation of Chinese soundex',
	author='IBM SystemT, IBM CODAIT',
	author_email='qian.kun@ibm.com, karthik.muthuraman@ibm.com, ihjhuo@ibm.com, frreiss@us.ibm.com',
	packages=['dimsim', 'dimsim.core', 'dimsim.utils', 'dimsim.data'],
	package_data={"":['pinyin_to_simplified.pickle','pinyin_to_traditional.pickle']},
	include_package_data=True,
	classifiers=["License :: OSI Approved :: Apache 2.0 License"],
	install_requires=[
        'pypinyin',
        ],
	test_suite='nose.collector',
    tests_require=['nose']
)
