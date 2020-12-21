import requests
import json

def get_reply(data):
    datas = {
        'reqType': 0,
        "perception": {
            "inputText": {
                "text": data
            },

            "selfInfo": {
                "location": {
                    "city": "武汉",
                    "province": "湖北"
                }
            }
        },

        "userInfo": {
        	# 这里填上自己的apiKey
            "apiKey": "*********************",
            # userid可以随便填写
            "userId": "443545"
        }
    }

    datas = json.dumps(datas)
    url = "http://openapi.tuling123.com/openapi/api/v2"
    r = requests.post(url=url, data=datas)
    return json.loads(r.text).get("results")[0].get("values").get("text")

