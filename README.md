
# How to upload your package to PyPI 

If you haven’t published things on PyPI before, you’ll need to create an account at [PyPI](https://pypi.org/).

We need you to create an account at [TestPyPI](https://test.pypi.org/) to test before you publish your package to PyPI. (You should set username and passwords PyPI same as TestPyPI)

# Picking A Name
Python module/package names should generally follow the following constraints:

* All lowercase
* Unique on PyPI
* Underscore-separated or no word separators at all 

# Creating The Scaffolding

Directory structure for <code>somsri</code> should look like this:
```
  grandmasomsri/
    setup.py
    REAME.md
    MANIFEST.in
    bin/
      somsri-run
    somsri/
      somsri.py
```
The subdirectory <code>somsri</code> is actually our Python module

<code>setup.py</code> contains:
```Python
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='somsri',
      packages=['somsri'],
      version='0.1',
      description='This is Grandma Somsri',
      long_description=readme(),
      url='https://github.com/SOMSRICAT/grandmasomsri',
      author='SomsriCat',
      author_email='your_email@example.com',
      license='Somsri',
      install_requires=[
          'datrie',
      ],
      scripts=['bin/somsri-run'],
      keywords='somsri',
      include_package_data=True,
      )
```

* In this package we use <code>datrie</code> that mean our package <code>somsri</code> depends on package <code>datrie</code> so we just add <code>install_requires</code> keyword argument
* Many Python packages include command line tools. This is useful for distributing support tools which are associated with a library 
for <code>somsri</code>, we will add a <code>somsri-run</code> command line tool by adding <code>scripts</code> keyword argument 
* You’ll probably want a README file in your source distribution, and that file can serve double purpose as the <code>long_description</code> specified to PyPI. Further, if that file is written in reStructuredText, it can be formatted nicely

The <code>somsri-run</code> script in <code>bin/somsri-run</code> looks like this:
```Python
#!/usr/bin/env python 

import somsri
print (somsri.printsomsri())
``` 
When we install the package, <code>setuptools</code> will copy the script to our PATH and make it available for general use:
```
$ somsri-run
```
<code>MANIFEST.in</code> contains:
```
include README.me
```

Now we can install the package locally (for use on our system or test before publish) with:
```
$ pip install .
```

# Publishing on TestPyPI and PyPI 

First create a source distribution with:
```
$ python setup.py sdist
```
This will create <code>dist/somsri-0.1.tar.gz</code> inside our top-level directory. 

You can use <code>twine</code> to upload the distribution packages. You’ll need to install <code>twine</code> by this command:
```
$ python3 -m pip install --user --upgrade twine
```

### TestPyPI
You should upload your package to TestPyPI before PyPI

Run Twine to upload all of the archives under dist:
```
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
You will be prompted for the username and password you registered with TestPyPI. 
After the command completes you can check your package at [TestPyPI](https://test.pypi.org/manage/projects/)

### PyPI
Now you ready to upload your package to PyPI
by following this command:
```
$ twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
You will be prompted for the username and password you registered with PyPI. 
After the command completes you can check your package at [PyPI](https://pypi.org/manage/projects/)

# Installing the Package

At this point, other consumers of this package can install the package with <code>pip</code>:
```
$ pip install somsri
```
It will be automatically installed to your Python package folder
