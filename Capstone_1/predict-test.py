import requests

url = 'http://localhost:9696/predict'

session_id = 'xyz-123'
session = {
    'Administrative': 9.0,
    'Administrative_Duration': 176.0,
    'BounceRates': 0.0,
    'Browser': 2.0,
    'ExitRates': 0.0,
    'Informational': 0.0,
    'Informational_Duration': 0.0,
    'Month': 5.0,
    'OperatingSystems': 2.0,
    'PageValues': 0.0,
    'ProductRelated': 28.0,
    'ProductRelated_Duration': 717.0,
    'Region': 5.0,
    'SpecialDay': 10.0,
    'TrafficType': 4.0,
    'VisitorType': 0.0,
    'Weekend': 1.0
}


response = requests.post(url, json=session).json()
print(response)

if response['revenue'] == 1:
    print('achieving the target revenue from session %s' % session_id)
else:
    print('not achieving the target revenue from session %s' % session_id)
