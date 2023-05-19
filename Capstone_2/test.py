import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://whyy.org/wp-content/uploads/2019/12/bright-daylight-environment-forest-240040-1-150x150.jpg'}

result = requests.post(url, json=data).json()
print(result)