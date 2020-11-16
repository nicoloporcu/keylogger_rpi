    
from pprint import pprint
import json
import requests

class rpiClient():

    def __init__(self, username, serv_address, serv_password):
        self.serv_password = serv_password
        self.username = username
        self.serv_address = serv_address
 


    def get_top5(self):

        response = requests.get("http://{}/top5".format(self.serv_address))

        # Print the JSON object from the HTTP response in a pretty format

        return response
