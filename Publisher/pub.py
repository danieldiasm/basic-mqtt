#!/usr/bin python3
# MQTT Simple Publisher
# Author: Daniel Z. Dias de Moraes (danieldiasm aka LeChevalier)

# NOTE: Parts of this sample code are copied from paho-mqtt docs, since there is no sense on changing it
# just for the sake of doing it again, I've kept it as it is.

# About:
# This is a python program meant to be a mqtt subscriber with server/broker configurations in another file.
# There will be a well commented program for me or anyone to consult anytime a refresher is needed.
# Useful links (should be moved to readme later):
# - Paho-MQTT:    https://pypi.org/project/paho-mqtt/
# - ConfigParser: https://docs.python.org/3/library/configparser.html


import configparser

import paho.mqtt.publish as publisher

# Config Parser
config = configparser.ConfigParser()
config.read('configs.cfg')

# Read from config file broker configs and set on vars
client_iden = str(config['BROKER']['ClientID'])
broker_addr = str(config['BROKER']['Address'])
broker_port = int(config['BROKER']['Port'])
broker_keep = int(config['BROKER']['Keepalive'])

# Get the topics from the configfile using list comprehension
topics = [topic for topic in config['TOPICS']]

# Paho publish function
def publish_msg(messages, baddr, bport, bkeep, cid):

    publisher.multiple(messages, hostname=baddr,
    port=bport, client_id=cid, keepalive=bkeep)

# Creates a message package and appends to a multiple
def make_message_pkg(package: list ,message: str, topic: str, qos: int, retain: bool):
    # The dict must be of the form:
    # msg = {‘topic’:”<topic>”, ‘payload’:”<payload>”, ‘qos’:<qos>, ‘retain’:<retain>}
    multiple = {}
    multiple["topic"]   = topic
    multiple["payload"] = message
    multiple["qos"]     = qos
    multiple["retain"]  = retain
    package.append(multiple)
    return package

msg_package = []

while True:
    # Asks user for an input
    to_publish = input("Type some message to have it published:")
    # Insert message to the queue
    msg_package = make_message_pkg(msg_package, to_publish, topics[0], 0, True)
    print()
    
    # If some more should be added or send it already
    more = input("Do you want to add some more? If not it will be sent. (0 for exit)")
    if more.lower() == 'y':
        pass
    elif more.lower() == 'n':
        print("Published message:")
        print(msg_package)
        
        publish_msg(msg_package, broker_addr, broker_port, broker_keep, client_iden)
        
        # Clear the queue
        msg_package = []
        print()
    elif more.lower() == "0":
        break
    else:
        print("Not valid, let's add some more!")
        print()
