# Complex condition checks  复杂条件判断

Conditional execution can be completed using the [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) statement.
条件判断使用if
`if` syntax  if 语法

```python
if expression:
    # code to execute
elif expression:
    # code to execute
else:
    # code to execute
```

[Boolean values](https://docs.python.org/3/library/stdtypes.html#boolean-values) can be either `False` or `True`  布尔类型值可以是`False` 或者 `True` 

[Boolean operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

- **x *or* y** - If either x **OR** y is true, the expression is executed   OR 标识x或者y有一个为真，则可以执行
- **x *and* y** - If x **AND** y are both true, the expression is executed  AND 标识只有x和y同时为真，才能执行

[Comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

- < less than
- < greater than
- == is equal to
- \>= greater than or equal to
- <= less than or equal to
- != not equal to
- **x *in* [a,b,c]** Does x match the value of a, b, or c
