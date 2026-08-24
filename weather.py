import requests
import csv
import os
from datetime import datetime

def get_city():
    city=input("Enter city: ").strip()
    return city

def get_country_code():
    country_code=input("Enter country code: ").strip().upper()
    return country_code

def check_not_empty_input(txt):
    return txt !="" 

def check_len_input(txt):
    return len(txt)==2

def raise_on_empty():
    raise ValueError("input ust not be empty")

def raise_on_len():
    raise ValueError("input most contine 2 letters")

def check_if_us(txt):
    return txt == "US"

def state_code():
    state_code=input("Enter_state_code: ")





