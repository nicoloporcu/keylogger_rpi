#import grovepi
import argparse
import time
import rpiTools  
import grovepi
import grove_rgb_lcd as lcd
import threading
potentiometer= 1
adc_ref = 5
grove_vcc = 5
full_angle = 300
word_list = []

def lcd_update():
    while True:
        potentiometer_read = grovepi.analogRead(potentiometer)
        voltage = round( (float) (potentiometer_read)* adc_ref /1023, 2)
        degrees = round(( voltage * full_angle) /grove_vcc, 2)
        level = int(degrees/full_angle * 5)
        if level >= len(word_list):
            level = len(word_list) -1
        print(word_list[level])
        lcd.setText_norefresh(str(level +1) + ": {:<13}".format(word_list[level][0]) + "\nTyped " + str(word_list[level][1]) + " times    \n")


def takeSecond(elem):
    return elem[1]


def main():
    global rpi_client
    rpi_client= rpiTools.rpiClient(args.u, args.a, args.p)
    t = threading.Thread(target = lcd_update)
    words = rpi_client.get_top5()
    t.start()
    while 1:
        words = rpi_client.get_top5()
        print(words.json())
        global word_list
        word_list = words.json()
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
