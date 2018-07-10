
# How to upload your package to PyPI 

If you haven’t published things on PyPI before, you’ll need to create an account at [PyPI](https://pypi.org/).

We need you to create an account at [TestPyPI](https://test.pypi.org/) to test before you publish your package to PyPI. (You should set username and passwords PyPI same as TestPyPI)

# Picking A Name
Python module/package names should generally follow the following constraints:

* All lowercase
* Unique on PyPI
* Underscore-separated or no word separators at all 

# Creating The Scaffolding

Directory structure for <code>grandmasomsri</code> should look like this:
```
  somsri/
    setup.py
    REAME.md
    MANIFEST.in
    bin/
        grandpaprayud-status
        grandmasomsri-status
        graph-power
    src/
        grandmasomsri/
            __init__.py
            grandmaSomsri.py
            grandpaPrayud.py
            graph/
                power.py
```
The subdirectory <code>grandmasomsri</code> is actually our Python module

<code>setup.py</code> contains:
```Python
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='grandmasomsri',
    version='0.1',
    description='Grandma Somsri and Grandpa Prayud',
    long_description=readme(),
    url='https://github.com/SOMSRICAT/grandmasomsri',
    author='SomsriCat',
    author_email='your_email@example.com',
    license='Somsri',
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    scripts=['bin/grandmasomsri-status',
             'bin/grandpaprayud-status',
             'bin/graph-power'],
    keywords='grandmasomsri grandpaprayud somsri prayud',
    packages=['grandmasomsri'],
    package_dir={'grandmasomsri': 'src/grandmasomsri'},
    package_data={'grandmasomsri': ['graph/*.py']
    },
)
```

* If your package required any package you needso add <code>install_requires</code> keyword argument to <code>setup.py</code> 
* Many Python packages include command line tools. This is useful for distributing support tools which are associated with a library 
for <code>grandmasomsri</code>, we will add a <code>grandmasomsri-status</code>, <code>grandpaprayud-status</code>, <code>graph-power</code>, command line tool by adding <code>scripts</code> keyword argument 
* You’ll probably want a README file in your source distribution, and that file can serve double purpose as the <code>long_description</code> specified to PyPI. Further, if that file is written in reStructuredText, it can be formatted nicely
* Package data can be added to packages using the <code>package_data</code> keyword argument to the setup() function
* Use <code>package_dir</code> key argument to path your package location
* Changed in version 3.1: All the files that match <code>package_data</code> will be added to the MANIFEST file if no template is provided. 


see more setup.py in the [PyPA sample project](https://github.com/pypa/sampleproject)

# Package
<code>grandmaSomsri.py</code> contains:
```Python
def somsri():
    print ("---------------------------------------------")
    print ("|                               /          |")
    print ("|                          ,.. /           |")
    print ("|                        ,'   ';           |")
    print ("|            ,,.__    _,' /';  .           |")
    print ("|           :','  ~~~~    '. '~            |")
    print ("|         :' (   )         )::,            |")
    print ("|         '. '. .=----=..-~  .;'           |")
    print ("|          '  ;'  ::   ':.  ''             |")
    print ("|           (:   ':    ;)                  |")
    print ("|            \\\  '    //'                  |")
    print ("|             ''      ''                   |")
    print ("---------------------------------------------")
    print ("|  Name: Grandma Somsri(ยายสมศรี)           |")
    print ("|  Ability: Very good eyesight (DEX +99)   |")
    print ("|  Weapon: Kar98k                          |")
    print ("|  Hobby: Camping in the forest            |")
    print ("---------------------------------------------")
```
<code>grandpaPrayud.py</code> contains:
```Python
def prayud():
    print ("---------------------------------------------")
    print ("|          ((  ####@@!!$$    ))             |")
    print ("|              `#####@@!$$`  ))             |")
    print ("|           ((  '####@!!$:                  |")
    print ("|         ((  ,####@!!$:   ))               |")
    print ("|             .###@!!$:                     |")
    print ("|             `##@@!$:                      |")
    print ("|               `#@!!$                      |")
    print ("|          !@#    `#@!$:       @#$          |")
    print ("|           #$     `#@!$:       !@!         |")
    print ("|                   '@!$:                   |")
    print ("|               '`\   !$: /`'               |")
    print ("|                   '\  '!: /'              |")
    print ("|                      '\ : /'              |")
    print ("---------------------------------------------")
    print ("|  Name: Grandpa Prayud(ตาประหยัด)           |")
    print ("|  Ability: Can get angry anytime           |") 
    print ("|           he want (str +99)               |")
    print ("|  Weapon: Table                            |")
    print ("|  Hobby: Do an exercise                    |")
    print ("---------------------------------------------")
```
```Python
import matplotlib.pyplot as plt
import numpy as np
import random

def powerGraph():
    y = np.arange(0,100)
    prayud = []
    somsri = []
    for i in y:
        tmp = i * 0.8
        if tmp % 3 == 0:
            tmp *= 1.2
        if tmp % 4 == 0:
            tmp *= 2
        prayud.append(tmp)

        tmp = i * 0.6
        if tmp % 4 == 0:
            tmp *= 1.1
        if tmp % 7 == 0:
            tmp *= 0.5
        if tmp % 6 == 0:
            tmp *= 2.5
        somsri.append(tmp)


    plt.plot(y,somsri,'-', label='Grandma Somsri')
    plt.plot(y,prayud, '-', label='Grandpa Prayud')
    plt.title("Power Graph")
    plt.xlabel('100 %')
    plt.ylabel('Power')

    plt.legend()

    plt.show()

powerGraph()
```
# Script
The <code>grandmasomsri-status</code> script in bin looks like this:
```Python
#!/usr/bin/env python 

from grandmasomsri.grandmaSomsri import somsri 

print (somsri())

``` 
The <code>grandpaprayud-status</code> script in bin looks like this:
```Python
#!/usr/bin/env python 

from grandmasomsri.grandpaPrayud import prayud 

print (prayud())

``` 
The <code>graph-power</code> script in bin looks like this:
```Python
#!/usr/bin/env python 

from grandmasomsri.graph import power

print (powerGraph())
``` 
<code>MANIFEST.in</code> contains:
```
include README.md
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
or
```
$ python3 setup.py sdist bdist_wheel
```
This will create <code>dist/grandmasomsri-0.1.tar.gz</code> inside our top-level directory. 

You can use <code>twine</code> to upload the distribution packages. You’ll need to install <code>twine</code> by this command:
```
$ pip install twine --upgrade
```
or 
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
$ pip install grandmasomsri
```


Its will be automatically installed to your Python package folder
and <code>setuptools</code> will copy the script to your PATH and make it available for general use

You can run package in command line by following this command:
```
$ grandmasomsri-status
```
```
$ grandpaprayud-status
```
```
$ graph-power
```
