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

