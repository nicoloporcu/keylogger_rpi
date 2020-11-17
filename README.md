# ee250_project

Team Members: Nicolo Porcu


VM dependencies (install these libraries before running):

```
pip3 install flask pyxhook argparse time
```

rPi dependencies:
```
pip3 install flask grovepi argparse threading time
```

Run the server on the RPI using the following command (-p 123 can be replaced by any password):
```
python3 keyloggerServer.py -p 123
```
While the server is running, run the following command on the VM to run the VM keylogger side:
```
python3 keyloggerClient.py -a <your pi ip address>:5000 -p 123 -u <your_username>
```
Run the following on the VM to display the top words!
```
python3 rpiClient.py -a localhost:5000 -p 123 -u <your_username>
```

Credit to these outside libraries: flask grovepi pyxhook
