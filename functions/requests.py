import requests
from const import MOORSE_URL, API_URL, AUTH_URL, DESTINATION_NUMBER, YOUR_TRIAL_NUMBER, GROUPID
from utils import json


class Requests(object):

    def __init__(self):

        pass

    def auth(self, user, password):
        payload = {'login': user, 'senha': password }
        headers = {'content-type': 'application/json'}
        response = requests.post(MOORSE_URL + AUTH_URL, verify=False, data=json.dumps(payload), headers=headers)
        response = json.to_json(response.text)
        return response['data']

    def send_message_to_contact(self, token, message):
        payload = {'from': YOUR_TRIAL_NUMBER, 'to': DESTINATION_NUMBER, 'body': message}
        response = requests.post(MOORSE_URL + API_URL+"/v2/whatsApp/sendMessage", verify=False, data=json.dumps(payload), headers={'content-type': 'application/json', 'Authorization': token})
        response = json.to_json(response.text)
        return response['data']

    def send_message_to_group(self, token, message):
        payload = {"groupId": GROUPID, "body": message}
        response = requests.post(MOORSE_URL + API_URL + "/v2/whatsApp/groups/sendMessage", verify=False, data=json.dumps(payload), headers={'content-type': 'application/json', 'Authorization': token})
        response = json.to_json(response.text)
        return response['data']