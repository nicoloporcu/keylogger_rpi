#import grovepi
import argparse
import time
import rpiTools  

def takeSecond(elem):
    return elem[1]


def main():
	global rpi_client
	rpi_client= rpiTools.rpiClient(args.u, args.a, args.p)

	while 1:
		words = rpi_client.get_top5()
		json_words = words.json()
		wlist = list(json_words.items())
		
		wlist.sort(key = takeSecond, reverse= True)
		wlist = wlist[:5]
		time.sleep(60)




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
