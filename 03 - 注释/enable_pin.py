#The enable_pin method is not coded yet  这里的enable_pin方法 并没有真正去实现
# I have created a dummy method so the code  我创建了一个模拟方法这样代码跑起来不会报错
# will run without an error
# Don't panic if you don't understand this part of the code 如果你还不明白这部分代码不要担心。
# we cover methods in a separate module      我们用单独的模块介绍方法。
def enable_pin(user, pin):
    print('pin enabled')

# Set current_user and pin to test values  设置当前用户和PIN码的测试值
current_user = 'TEST123'
pin = '123456'

# Enable PIN check as listed in
# security requirements
enable_pin(current_user, pin)

