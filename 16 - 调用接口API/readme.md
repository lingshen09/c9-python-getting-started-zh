# Calling APIs  调用API

You can call functions called by other programs hosted on web servers. 你可以通过API调用其他网页服务的程序
[Microsoft Azure Cognitive Services](https://docs.microsoft.com/en-ca/azure/cognitive-services/) contain a number of APIs you can call from your code to add intelligence to your apps and websites.
微软AZURE服务包含许多你可以在应用和网页中使用的API
In the code example you call the [Analyze Image](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa0) function of the [Computer Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
在代码示例中你可以调用计算机视觉的图片分析方法
Calling the API requires   调用API你需要
- [API Key](https://azure.microsoft.com/en-ca/try/cognitive-services/) to give you permission to call the API  获取API的授权密钥
- Address or Endpoint of the service   服务的网络地址
- function name of method to call as listed in the [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa) API文档中的方法名
- function parameters as listed in the [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa) API文档中的方法参数
- HTTP Headers as listed in the [API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa) API文档中的HTTP请求头

