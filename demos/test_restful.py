
import json

import requests


def get():
    
    # Authorization:	Bearer eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjo0fQ:1Y2Uub:3orH7K2zTGxq7WKqL5Mc2IqrPtY
    # X-Session-Id:	3d9a0086c1e10caba5b2b2d0debcac0dbcb0723c
    headers = {"Authorization":"Bearer eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjo0fQ:1Y2Uub:3orH7K2zTGxq7WKqL5Mc2IqrPtY",
        "X-Session-Id":"3d9a0086c1e10caba5b2b2d0debcac0dbcb0723c"}
    r = requests.get('http://127.0.0.1:6230/v1/sign-in', headers = headers)

    #print dir(r)
    print "get:"
    print r.status_code
    print r.headers#['allow']
    print r.text
    print r.json()
    print r.cookies.items()
    

def post():
    body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    url = "http://127.0.0.1:6230/v2/sign-in"
    r = requests.post(url=url, data=body)
    
    print r.headers
    print r.text

def put():
    body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    url = "http://127.0.0.1:6230/v2/sign-in"
    r = requests.put(url=url, data=body)
    
    print r.headers
    print r.text
    
def patch():
    body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    url = "http://127.0.0.1:6230/v2/sign-in"
    r = requests.patch(url=url, data=body)
    
    print r.headers
    print r.text

def head():
    #body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    url = "http://127.0.0.1:6230/v2/sign-in"
    r = requests.head(url=url) #, data=body
    print ">head:"
    print r.headers
    print r.text
    
def options():
    body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    url = "http://127.0.0.1:6230/v2/sign-in"
    r = requests.options(url=url, data=body)
    
    print r.headers
    print r.text
    
def delete():
    body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    url = "http://127.0.0.1:6230/v2/sign-in"
    r = requests.delete(url=url, data=body)
    
    print r.headers
    print r.text

if __name__ == "__main__":
    
    get()
    post()
    put()
    patch()
    head()
    options()
    delete()


