

#pip install requests
import requests, json
from requests.auth import HTTPBasicAuth
data = {
    "urls": ["https://s3-us-west-2.amazonaws.com/nanonets/replace_me.jpg"], \
    "modelId":"f89214c9-2135-4ad3-99f0-c0c4cabf1d5a"
}

headers = {
    'accept': 'application/x-www-form-urlencoded'
}


url = "https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/"
r = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('Ltf_zwZgg3dFLEAGkQ_sYrzvNF7BcdHi', ''))
print r.content

