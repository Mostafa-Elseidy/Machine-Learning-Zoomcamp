import requests

# Invoke URL: https://socxqf1v1c.execute-api.us-east-1.amazonaws.com/test
# add /predict to the url generated from AWS Gateway API
url = 'https://socxqf1v1c.execute-api.us-east-1.amazonaws.com/test/predict'

data = {'url': 'https://whyy.org/wp-content/uploads/2019/12/bright-daylight-environment-forest-240040-1-150x150.jpg'}

result = requests.post(url, json=data).json()
print(result)