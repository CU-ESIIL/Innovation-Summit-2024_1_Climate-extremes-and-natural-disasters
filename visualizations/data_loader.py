## DEM data
import os.path
import sys
from subprocess import call
import datetime
import time
import csv
import socket
import smtplib
import requests


fema_dir="/data"
fema_file_url = "" # TODO 

### this method loads data from http request
### Assumes you have already loaded the file to the discovery environment 
### Destination file name is the name of the file that will be loaded to /data directory
def load_file(destination_file_name, url):
    data_destination = '../data/' + destination_file_name
    url = fema_file_url + fname
    r = requests.get(url)
    open(file_name , 'wb').write(r.content)
    
def subset(): 
    pass


