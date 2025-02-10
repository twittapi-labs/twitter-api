from setuptools import setup, find_packages

with open('README.md', 'r') as file:
  long_description = file.read()

setup(
  name='twittapi',
  version='0.1.0',
  author='twittapi',
  author_email='twittapi.work@gmail.com',
  packages=find_packages(),
  license='MIT',
  install_requires=[
    'requests',
  ],
  description='Unofficial Twitter API In Python',
  long_description=long_description,
  long_description_content_type='text/markdown',
  keywords=['twitter', 'api', 'unofficial', 'python', 'twittapi'],
)