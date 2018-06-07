from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='grandmasomsri',
      version='0.2',
      description='Grandma Somsri and Moy',
      long_description=readme(),
      url='https://github.com/SOMSRICAT/grandmasomsri',
      author='SomsriCat',
      author_email='your_email@example.com',
      license='Somsri',
      install_requires=[
          'datrie',
      ],
       scripts=['bin/grandmasomsri-run'],
       keywords='somsri grandmasomsri grandma',
       packages=['grandmasomsri'],
       package_dir={'grandmasomsri': 'src/grandmasomsri'},
       package_data={'grandmasomsri': ['text/*.txt']},
       )


