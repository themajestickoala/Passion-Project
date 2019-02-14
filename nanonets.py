import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://app.nanonets.com/api/v2/ObjectDetection/Model'
MODEL_ID = 'ca57f806-5472-40db-ac7a-b2898be45f20'


def send_image_to_api(image_url):
    data = {'urls': [image_url]}

    headers = {'accept': 'application/x-www-form-urlencoded'}

    url = '{}/{}/LabelUrls/'.format(BASE_URL, MODEL_ID)
    auth = HTTPBasicAuth('Ltf_zwZgg3dFLEAGkQ_sYrzvNF7BcdHi', '')

    r = requests.post(url, headers=headers, data=data, auth=auth)

    print(r.status_code)

    return r.json()
