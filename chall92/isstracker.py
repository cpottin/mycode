#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    timestamp = datetime.datetime.now()

    print("The current location of the ISS is....")
    print("Longitude: " , lon)
    print("Latitude: ", lat)
    print("Timestamp: ", timestamp) 



if __name__ == "__main__":
    main()

