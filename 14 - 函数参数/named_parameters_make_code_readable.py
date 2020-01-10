# Create a function to handle errors that occur during code execution  创建一个处理错误的方法
# This will display a message to the user adn may log the error for the support team to 这个方法给用户显示出错误的消息方便团队调试
# help with debugging
# 
# Parameters:  参数
#   error_code: Unique error code assigned to each type of error: e.g. 45 is datatype conversion error  错误码：独特的错误编码比如45 代表数据类型转换错误
#   error_severity: 0 - fatal error should never occur                                  错误严重级别：0 -致命错误 永不应该发生
#                   1 - severe error code cannot continue                                             1 - 服务错误不能继续执行
#                   2 - warning code can continue but may be missing information in records           2 - 警告错误，可以继续执行但会导致记录丢失信息        
#   log_to_db: Should this error be logged to the database                                 log_to_db： 这些错误是否记录到数据库   
#   error_message: Error message to display to user and write to database                  error_message: 错误消息描述
#   source_module: Name of the python module that generated ther error                     source_module: Python模块中产生错误的模块名

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    # Imagine code here that logs our error to a database or file  假设这里的代码产生错误并记录到数据库或文件中

first_number = 10
second_number = 5
    # This function call by itself is confusing, I have to look at the 这样的方法调用让人迷惑，必须去看定义才能理解
    # definition of the error_logger function to understand it
if first_number > second_number:
    error_logger(45,1,True,'Second number greater than first','adding_method')


if first_number > second_number:
    # This function call by itself is easier to understand because I can  这样调用让人更容易理解传入的参数
    # see how the values I pass in map to the function parameters
    error_logger(error_code=45, 
                 error_severity=1,
                 log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='adding_method')
