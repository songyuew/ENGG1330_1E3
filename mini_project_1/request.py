import http.client
import json

def getRates():
    conn = http.client.HTTPSConnection("api.hsbc.com.hk")
    payload = ''
    headers = {
    'ClientID': '6e5da8a0-3748-4d38-9e6d-714eb67e4eaa',
    'ClientSecret': 'SzUzlne-4nMEcRK_0d2W-HIZulbWZr7FXPgnaQ0WFtOObxGGM8sDQGt6QOvPST1RMnq8K2aiEg6oIrhFIs8nhQ'
    }
    conn.request("GET", "/live/open-banking/v1.0/personal-foreign-exchange-rates", payload, headers)
    res = conn.getresponse()
    return json.load(res)