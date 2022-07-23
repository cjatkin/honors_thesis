#commander code for gui to connect to
#from gui import ip_address_entered
#the... .commands??

import redis
import sys
import json
from time import sleep
#import fun as foo
import goo as foo
import subprocess
#from gui import get_ip

def hello():
    print("hello from commander!")

'''
def connect(ip_address):
    #ip_address_entered = ip_address.get()
    #ip_address = get_ip()
    print(ip_address)
    print('connect pressed')
'''
def commands_list():
    # load firmware config
    # lambda method use for general purpose firmware loading
    f = "goo" # can be a user input
    jsonpath = lambda name : "./" + name + "/" + name + ".json"
    cmdpath = lambda name : "./" + name + "/" + name + ".py"

    # Reading JSON File
    with open(jsonpath(f),'r') as cmdlist:
        command_obj = cmdlist.read()
    command_dict = json.loads(command_obj)
    #connects variable command_dict to fun.py/.json and can be used to reference
    #   either file

    # PART 3 ##################################################
    print("Command List:")
    print(35*"-")
    for c in command_dict:
        print(f"{c} | cmd: {command_dict[c]} ") #will only have one command (00: funHello)
    print("\n")

def check_chnls():
    chnls_open = r.pubsub_channels()
    chnls_open = [chnl.decode() for chnl in chnls_open]
    return chnls_open

def userInput():
    chnls_open = check_chnls()
    print(f"Open channels: \'{chnls_open}\'...")

    if len(chnls_open) == 0:
        print("Need drones to subscribe to a channel...")
        animation = "|/-\\"
        i=0
        while len(chnls_open) == 0:
            sleep(0.1)
            sys.stdout.write("\rWaiting for subscription... "+animation[i%4])
            sys.stdout.flush()
            i+=1
            chnls_open = check_chnls()
    while True:
        #p.subscribe('borg') # Channel which drones publish to confirming recieved commands
        p.subscribe('python-channel') # Channel which drones publish to confirming recieved commands
        chnls_open = check_chnls()
        drone = str(input("Which channel would you like to publish to? \n"+str(chnls_open)+'\n'))
        try:
            if drone in chnls_open:
                print("Publishing to " + str(drone))
                while True:
                    print("Command List:")
                    print(35*"-")
                    for c in command_dict:
                        print(f"{c} | cmd: {command_dict[c]} ")
                    print("\n")
                    print("To select a different drone enter 'change'.")
                    command = str(input("Enter command from list.   "))
                    try:
                        if command == 'stop':
                            r.publish(drone,command)
                            break
                        elif command == 'change':
                            print("Changing drone selection...")
                            break
                        elif hasattr(foo,command_dict[command]):
                            print(f"Sending \'{command_dict[command]}\' Command.\n")
                            r.publish(drone,command)
                            print("Sent")
                            while True:
                                msg = p.get_message()
                                if msg:
                                    print(msg['data'].decode())
                                    break
                        else:
                            print("Invalid command.")
                        sleep(0.1)
                    except KeyError:
                        print("Please enter a valid key.")
                if command == 'stop':
                    break # Breaks the outer while loop
                else:
                    continue
            elif drone == 'stop':
                break
            else:
                print("Try a different channel.")
        except ValueError:
            print("Invalid input")
    print("Exiting Commander")

'''
def get_ip():
    return str(input("\nEnter ip address: "))
'''
#this function connects and subscribes user to redis channel


def connect(ip_address):

    print(ip_address)
    print('connect pressed')

    chnl ="python-channel"
    chnl2 = "borg"
    print(f"Subscribing to \'{chnl}\'...")

    r = redis.Redis(host=ip_address)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(chnl)			#drone subscribes to channel here
    print(f"Subscribed to \'{chnl}\'.\n")


    userInput()
