#!/usr/bin python3
# MQTT Simple Subscriber
# Author: Daniel Z. Dias de Moraes (danieldiasm aka LeChevalier)

# NOTE: Parts of this sample code are copied from paho-mqtt docs, since there is no sense on changing it
# just for the sake of doing it again, I've kept it as it is.

# About:
# This is a python program meant to be a mqtt subscriber with server/broker configurations in another file.
# There will be a well commented program for me or anyone to consult anytime a refresher is needed.
# Useful links (should be moved to readme later):
# - Paho-MQTT:    https://pypi.org/project/paho-mqtt/
# - ConfigParser: https://docs.python.org/3/library/configparser.html

# Later implementations:
# Bind Address - Config Parser and Paho

import configparser

import paho.mqtt.client as mqtt

# Config Parser
config = configparser.ConfigParser()
config.read('configs.cfg')

# Read from config file broker configs and set on vars
broker_addr = str(config['BROKER']['Address'])
broker_port = int(config['BROKER']['Port'])
broker_keep = int(config['BROKER']['Keepalive'])

# Get the topics from the configfile using list comprehension
topics = [topic for topic in config['TOPICS']]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code "+str(rc))
    global topics

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for topic in topics:
        client.subscribe(topic)
        print(f"Subscribed on: {topic}")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# Paho inital setup
client = mqtt.Client()

# Set Callbacks to client
# It goes like this: client.on_this_event = call_this_function
client.on_connect = on_connect
client.on_message = on_message

# Now asks it for connecting effectively
client.connect(broker_addr, broker_port, broker_keep)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()