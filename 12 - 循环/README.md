# Loops  循环

## For loops  For循环

[For loops](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) takes each item in an array or collection in order, and assigns it to the variable you define.
for循环按顺序遍历一个数组种每个元素，按你定义方式操作它
``` python
names = ['Christopher', 'Susan']
for name in names:
    print(name)
```

## While loops  While循环

[While loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) perform an operation as long as a condition is true.
While循环一直执行某个动作直到判断条件为真
``` python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1
```
