from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
        
setup(name='yugioh',
      version='0.0.26',
      description='Yu-Gi-Oh API Wrapper',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/IThinkImOKAY/yugioh',
      author='diogenesjunior',
      author_email='diogenesjunior@protonmail.com',
      install_requires=['requests'],
      packages=['yugioh'],
      keywords='Yu-Gi-Oh API')
