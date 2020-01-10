x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere  可选择在某处打印出e信息
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')
