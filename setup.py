from setuptools import setup

setup(name='yugioh',
      version='0.0.26',
      description='Yu-Gi-Oh API Wrapper',
      long_description=open('README.rst').read(),
      url='https://github.com/IThinkImOKAY/yugioh',
      author='diogenesjunior',
      author_email='diogenesjunior@protonmail.com',
      install_requires=['requests'],
      packages=['yugioh'],
      keywords='Yu-Gi-Oh API')
