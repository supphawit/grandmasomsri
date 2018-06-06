from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='somsri',
      version='0.2',
      description='Grandma Somsri sell bear',
      long_description=readme(),
      url='https://github.com/SOMSRICAT/grandmasomsri',
      author='SomsriCat',
      author_email='your_email@example.com',
      license='Somsri',
      packages=['somsri'],
      install_requires=[
          'datrie',
      ],
       scripts=['bin/somsri-run'],
       keywords='somsri',
       include_package_data=True,
       )


