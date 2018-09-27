#!/usr/bin/env 
# @author: Raghuvar

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

#Defining the App
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=2))

    res = resultWebHook(req)

    res = json.dumps(res, indent=2)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def resultWebHook(req):
    if req.get("queryResult").get("action") != "firstname":
        return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    fname = parameters.get("first_name")

    name_detail = {'first_name':'Srianth'}

    statement = "First Name is" + " " + str(name_detail['first_name'])
    print("Response:")
    print(statement)
    return {
        "statement": statement,
        "displayText": statement,
        "source": "firstname"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print ("App has been started on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')
