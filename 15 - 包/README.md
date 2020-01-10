# Packages and modules  包和模块

## Modules  模块

[Modules](https://docs.python.org/3/tutorial/modules.html) allow you to store reusable blocks of code, such as functions, in separate files. They're referenced by using the `import` statement.
模块时你将可重用的代码块如函数方法，放在不同的文件中。他们通过import语句引入。
``` python
# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')
```

## Packages 包

[Distribution packages](https://packaging.python.org/glossary/#term-distribution-package) are external archive files which contain resources such as classes and functions. Most every application you create will make use of one or more packages. Imports from packages follow the same syntax as modules you've created. The [Python Package index](https://pypi.org/) contains a full list of packages you can install using [pip](https://pip.pypa.io/en/stable/).
包是包含一系列的类和方法。通常你的应用会包含一个或更多个包。引用包和使用模块的语法类似。Python包管理pypi包含了你可以安装使用的大量的包。
## Virtual environments 虚环境

[Virtual environments](https://docs.python.org/3.7/library/exceptions.html) allow you to install packages into an isolated folder. This allows you to better manage versions.
虚环境让你在隔离的文件夹中配置包，这使得你版本管理更容易。
``` console

```
