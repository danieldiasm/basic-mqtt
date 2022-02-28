#!/usr/bin python3
# MQTT Subscriber Sample
# Author: Daniel Z. Dias de Moraes (danieldiasm aka LeChevalier)
# About:
# This is a python program meant to be a mqtt subscriber with server/broker configurations in another file.
# There will be a well commented program for me or anyone to consult anytime a refresher is needed.
# Useful links (should be moved to readme later):
# - Paho-MQTT:    https://pypi.org/project/paho-mqtt/
# - ConfigParser: https://docs.python.org/3/library/configparser.html

import configparser

import paho

config = configparser.ConfigParser()
config.read('configuration.cfg')

# Read from config file broker configs and set on vars
broker_addr = config['BROKER']['Address']
broker_port = config['BROKER']['Port']
broker_keep = config['BROKER']['Keepalive']

# If there is any bind address, set it - TO BE IMPLEMENTED LATER
# if  config['BROKER']['Bind_Address'] is not "":
#     broker_bind = config['BROKER']['Bind_Address']

# Get the topics from the configfile using list comprehension
topics = [topic for topic in config['TOPICS']]
print(topics)