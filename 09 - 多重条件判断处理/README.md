# Handling conditions  条件判断处理

Conditional execution can be completed using the [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) statement. Adding `elif` allows you to check multiple conditions
通过If语句处理条件时，加上elif可以处理多重条件判断
`if` syntax  if 语法格式：

```python
if expression:
    # code to execute
elif expression:
    # code to execute
else:
    # code to execute
```

[Boolean operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

- **x *or* y** - If either x OR y is true, the expression is executed  x or y 标识x或者y条件有一个为真，则会继续执行

[Comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

- < less than
- < greater than
- == is equal to
- \>= greater than or equal to
- <= less than or equal to
- != not equal to
- **x *in* [a,b,c]** Does x match the value of a, b, or c   x in [a,b,c] 标识x是否匹配a\b\c中任意一个
