
import time
import json

import requests


#"eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjo0fQ:1Y2YOj:bA5J-vvdbJWRxJb4vLwdLcameU8"

print time.time()

def post():
    
    data = {"username":"admin","password":"123123","type":"normal"}
    
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    body = json.dumps(data)
    
    #url = "http://127.0.0.1:6231/"
    
    url = "http://localhost:8000/api/v1/auth"
    
    
    start = time.time()
    r = requests.post(url=url, data=body, headers = headers)
    print "time:", time.time() - start
    print r.headers
    print "text:", r.text


def auth():
    
    data = {"username":"admin","password":"123123","grant_type":"password",
        "client_id":101,"client_secret":"secret"
        }
    
    headers = {"Content-Type": "application/json; charset=UTF-8",
        # "Authorization":"Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW"
    }
    body = json.dumps(data)
    
    url = "http://127.0.0.1:6231/oauth/token"
    
    #url = "http://localhost:8000/api/v1/auth"
    
    
    start = time.time()
    r = requests.post(url=url, data=body, headers = headers)
    print "time:", time.time() - start
    print r.headers
    print dir(r)
    print r.status_code
    print r.cookies
    print r.elapsed
    print "text:", r.text

    
if __name__ == "__main__":
    #post()
    auth()