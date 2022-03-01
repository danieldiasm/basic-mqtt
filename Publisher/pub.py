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
client_name = str(config['BROKER']['ClientID'])
broker_addr = str(config['BROKER']['Address'])
broker_port = int(config['BROKER']['Port'])
broker_keep = int(config['BROKER']['Keepalive'])

# Get the topics from the configfile using list comprehension
topics = [topic for topic in config['TOPICS']]

# Paho publish function
def publish_msg(messages, topic):
    # This should become a dict later (kargs maybe)
    global broker_addr, broker_port, broker_keep

    publisher.multiple(messages, hostname=broker_addr,
    port=broker_port, client_id="", keepalive=broker_keep)


