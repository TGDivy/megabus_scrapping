# Webscrapper for megabus.com

import requests
from bs4 import BeautifulSoup
import json
import os
import time
import datetime
import sys
import re

# Global variables
# URL to scrape
base_url = "https://uk.megabus.com/journey-planner/journeys"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


# Given base url and params, return a url
def convert_url(base_url, params):
    url = base_url + "?"
    for key, value in params.items():
        url += f"{key}={value}&"
    url = url[:-1]
    return url


# Accept diferrent parameters and return a url
def get_url(
    departureDate="2023-02-09",
    destinationId="58",
    originId="34",
    totalPassengers="1",
):
    params = {
        "days": 1,
        "concessionCount": "0",
        "departureDate": departureDate,
        "destinationId": destinationId,
        "inboundOtherDisabilityCount": "0",
        "inboundPcaCount": "0",
        "inboundWheelchairSeated": "0",
        "nusCount": "0",
        "originId": originId,
        "otherDisabilityCount": "0",
        "pcaCount": "0",
        "totalPassengers": totalPassengers,
        "wheelchairSeated": "0",
    }
    url = convert_url(base_url, params)
    return url


# Get Journey data
def get_journey_data(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Get the json data from the html window.SEARCH_RESULTS
    json_data = soup.find("script", text=re.compile("window.SEARCH_RESULTS")).string

    # Remove the window.SEARCH_RESULTS = from the string
    json_data = json_data.replace("window.SEARCH_RESULTS = ", "").strip()
    # Remove the ; from the end of the string if it exists
    if json_data[-1] == ";":
        json_data = json_data[:-1]

    # Convert the string to a json object
    json_data = json.loads(json_data)

    return json_data


if __name__ == "__main__":
    # Get the urls for this week
    # Get the data for each url, and save create a object for each day
    # Save the data to a json file
    data = {}
    for i in range(7):
        date = datetime.datetime.now() + datetime.timedelta(days=i)
        date = date.strftime("%Y-%m-%d")
        url = get_url(departureDate=date)

        # Get the data for this url
        json_data = get_journey_data(url)

        # Save the data to the data object
        data[date] = json_data

    # Save the data to a json file
    with open("data.json", "w") as f:
        json.dump(data, f)
