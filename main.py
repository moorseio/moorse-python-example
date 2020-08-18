from const import MESSAGE, USER, PASSWORD, MESSAGE_GROUP
from functions.requests import Requests
import json

def main():
    requests = Requests()
    token = requests.auth(USER, PASSWORD)
    message = requests.send_message_to_contact(token, MESSAGE)
    print(message)
    messageGroup = requests.send_message_to_group(token, MESSAGE_GROUP)
    print(messageGroup)

main()
