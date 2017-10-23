import requests
import json
import random

def send_sms_to_mobile(mobile_number,token):
    url = "https://api.kavenegar.com/v1/2B4A562F475135393038794464546B492F4152374B773D3D/verify/lookup.json"
    data = {}
    data['receptor']=mobile_number
    data['token']= token
    data['template']="verify"
    r = requests.post(url, data)
    output = json.loads(r.text)

    if output['return']['status'] != 200 :
        #log the error in the database
        #print "Error"
        #print r.text
        return 1

    else:
        #print "message send successfully"
        return 0
