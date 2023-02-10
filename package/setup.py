from setuptools import setup, find_packages

setup(name='autotarget',

version='1.0.0.3',

description='A Disease-Associated Drug Target Recommendation System using Node Classification with Neighborhood Context in PPI Networks',

author='Hyunseung Kong',

author_email='hskong@snu.ac.kr',

url='https://github.com/gumgo91/AutoTarget',

license='MIT',

py_modules=['autotarget'],

python_requires='>=3',

install_requires=[],

packages=['autotarget'],
package_data={'autotarget': ['data/*']}
)