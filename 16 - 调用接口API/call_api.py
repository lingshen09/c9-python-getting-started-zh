# This code will show you how to call the Computer Vision API from Python  下面的代码展示怎么调用计算机视觉API
# You can find documentation on the Computer Vision Analyze Image method here 你可以在下面的文档中找到
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python  使用requests库调用Python的RESTful接口
import requests

# We will need the json library to read the data passed back  我们需要使用json库读取返回数据
# by the web service
import json

# You need to update the SUBSCRIPTION_KEY to   你需要将下面的密钥更新为你自己的计算机视觉服务的密钥
# they key for your Computer Vision Service
SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

# You need to update the vision_service_address to the address of 你也需要将下面的请求地址更新为你自己的
# your Computer Vision Service
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

# Add the name of the function you want to call to the address  加上你要调用的方法
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function   根据文档需要配置三个可选参数language, details & visualFeature
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# Open the image file to get a file object containing the image to analyze  打开测试图片
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function  根据文档我们构建一个HTTP的请求头
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function  根据文档我们使用POST方法请求调用
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code  做好错误处理
response.raise_for_status()

# Display the JSON results returned   展示JSON的返回值
results = response.json()
print(json.dumps(results))
