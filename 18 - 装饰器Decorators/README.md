# Decorators  装饰器

[Decorators](https://www.python.org/dev/peps/pep-0318/) are similar to attributes in that they add meaning or functionality to blocks of code in Python. They're frequently used in frameworks such as [Flask](http://flask.pocoo.org/) or [Django](https://www.djangoproject.com/). The most common interaction you'll have with decorators as a Python developer is through using them rather than creating them.
装饰器是将一个有意义的或者功能性的代码块包装起来。他们被大量使用在flask和django框架中。通常你使用他们多过创建他们。
``` python
# Example decorator
@log(True)
def sample_function():
    print('this is a sample function')
```
