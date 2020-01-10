# Function parameters  方法的参数

Functions allow you to take code that is repeated and move it to a module that can be called when needed. Functions are defined with the `def` keyword and must be declared before the function is called in your code. Functions can accept one or more parameters and return values.
方法允许你将重复操作合并如一个模块再调用。方法通过关键字def定义，并且先定义再调用。方法可以接收参数并给出返回值。
- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

```python
def function_name(parameter):
    # code to execute
    return value
```

Parameters can be assigned a [default value](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) making them optional when the function is called.
参数可以配置默认值
```python
def function_name(parameter=default):
    # code to execute
    return value
```

When you call a function you may specify the values for the parameters using positional or [named notation](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
当你调用方法时可以根据位置传入参数或指定参数名
```python
def function_name(parameter1, parameter2):
    # code to execute
    return value

# Positional notation pass in arguments in same order as parameters are declared
result = function_name(value1,value2)

# Named notation
result = function_name(parameter1=value1, parameter2=value2)
```
