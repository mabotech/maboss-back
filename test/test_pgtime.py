

import requests

import unittest

import json

class TestPoc(unittest.TestCase):
    
    def setUp(self):
        
        pass
        
      
    def test_pgtime(self):
        
        url = 'http://127.0.0.1:6226/api/v1/callproc.pgtime'
        
        payload = {"name":"mtp_find_cf1", "ver":"V1.1"}
        headers = {'content-type': 'application/json', 'accept':'json','User-Agent':'mabo'}
        #headers = {'Accept':'json'}
        #payload = json.dumps(payload)
        
        r = requests.post(url, data =   payload , headers={})
        print  r.headers
        #v = r.text #json.loads(r.text)
        print r.text
        """
        assert r.status_code == 500
        assert r.reason == 'Internal Server Error'
        assert r.text == 'error in poc'
        """
        
        
    def test_call(self):
        
        url = 'http://127.0.0.1:6226/api/v1/callproc.call'
        
        payload = {
                        "jsonrpc":"2.0",
                        "id":"r2",
                        
                        "params":
                        {
                            "method":"mtp_upsert_cf6",
                            "table":"calendar_day", 
                            "columns":{
                            "id":"2",
                            "rowversion":2,
                            "hours":8.1
                            },
                           "context":{"user":"idea", "languageid":"1033", "sessionid":"123" } 
                       }
                    }
                    
        headers = {'content-type': 'application/json', 'accept':'json','User-Agent':'mabo'}
        #headers = {'Accept':'json'}
        payload = json.dumps(payload)
        
        r = requests.post(url, data =   payload , headers=headers)
        #print  r.headers
        #v = r.text #json.loads(r.text)
        print r.text
        """
        assert r.status_code == 500
        assert r.reason == 'Internal Server Error'
        assert r.text == 'error in poc'
        """
        
if __name__ == "__main__":
    
    unittest.main()