from setuptools import setup

setup(
   name='_bot',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='sadykov.fandas@gmail..com',
   packages=['_bot'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
)
