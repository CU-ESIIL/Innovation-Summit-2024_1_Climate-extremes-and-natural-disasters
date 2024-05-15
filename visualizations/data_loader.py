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




### this method loads data from http request
### Assumes you have already loaded the file to the discovery environment 
### Destination file name is the name of the file that will be loaded to /data directory
def load_file(file_name):
    data_path = 'Innovation-Summit-2024_1_Climate-extremes-and-natural-disasters/data' 
    # Use os.path to read file into memory
    file_path = os.path.join(data_path, file_name)
    with open(file_path, 'r') as file:
        data = file.read()

def subset(): 
    pass


